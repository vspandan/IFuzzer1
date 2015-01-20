#!/usr/bin/env python

# Test harness for JSTests, controlled by manifest files.

import datetime, os, sys, subprocess
from subprocess import *

from mozillaJSTestSuite.tests import TestResult, NullTestOutput
from mozillaJSTestSuite.workers import Source
from mozillaJSTestSuite.progressbar import ProgressBar
from os.path import abspath

from GECodeGenerator import runFuzzer 
from langparser.AntlrParser import AntlrParser

import threading
import multiprocessing
from _collections import defaultdict

def exclude_tests(test_list, exclude_files):
    exclude_paths = []
    for filename in exclude_files:
        for line in open(filename):
            if line.startswith('#'): continue
            line = line.strip('\n')
            if not line: continue
            exclude_paths.append(line)
    return [ _ for _ in test_list if _.path not in exclude_paths ]

def check_manifest(test_list):
    test_set = set([ _.path for _ in test_list ])

    missing = []

    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if dirpath == '.': continue
            if not filename.endswith('.js'): continue
            if filename in ('browser.js', 'shell.js', 'jsref.js', 'template.js'): continue

            path = os.path.join(dirpath, filename)
            if path.startswith('./'):
                path = path[2:]
            if path not in test_set:
                missing.append(path)

    if missing:
        print "Test files not contained in any manifest:"
        for path in missing:
            print path
    else:
        print 'All test files are listed in manifests'

class TestTask:
    js_cmd_prefix = None

    def __init__(self, test, options):
        self.test = test
        self.options = options

    def __call__(self):
        if self.test.enable or self.options.run_skipped:
            return self.test.run(self.js_cmd_prefix, self.options.timeout)
        else:
            return NullTestOutput(self.test)

    def __str__(self):
        return str(self.test)

    @classmethod
    def set_js_cmd_prefix(self, js_path, js_args, debugger_prefix):
        parts = []
        if debugger_prefix:
            parts += debugger_prefix
        parts.append(js_path)
        if js_args:
            parts += js_args
        self.js_cmd_prefix = parts

class ResultsSink:
    output_file = None

    def __init__(self):
        self.groups = {}
        self.counts = [ 0, 0, 0 ]
        self.n = 0

        self.finished = False
        self.pb = None

    def push(self, output, options):
        if isinstance(output, NullTestOutput):
            if options.tinderbox:
                print '%s | %s (SKIP)' % ('TEST-KNOWN-FAIL', output.test.path)
            self.counts[2] += 1
            self.n += 1
        else:
            if options.show_cmd:
                print >> self.output_file, subprocess.list2cmdline(output.cmd)

            if options.show_output:
                print >> self.output_file, '    rc = %d, run time = %f' % (output.rc, output.dt)
                self.output_file.write(output.out)
                self.output_file.write(output.err)

            result = TestResult.from_output(output)
            tup = (result.result, result.test.expect, result.test.random)
            dev_label = self.LABELS[tup][1]
            self.groups.setdefault(dev_label, []).append(result.test.path)

            self.n += 1

            if result.result == TestResult.PASS and not result.test.random:
                self.counts[0] += 1
            elif result.test.expect and not result.test.random:
                self.counts[1] += 1
            else:
                self.counts[2] += 1

            if options.tinderbox:
                if len(result.results) > 1:
                    for sub_ok, msg in result.results:
                        label = self.LABELS[(sub_ok, result.test.expect, result.test.random)][0]
                        if label == 'TEST-UNEXPECTED-PASS':
                            label = 'TEST-PASS (EXPECTED RANDOM)'
                        print '%s | %s | %s' % (label, result.test.path, msg)
                print '%s | %s' % (self.LABELS[(result.result,
                                              result.test.expect, result.test.random)][0],
                                 result.test.path)
           
        if self.pb:
            self.pb.label = '[%4d|%4d|%4d]' % tuple(self.counts)
            self.pb.update(self.n)

    # Conceptually, this maps (test result x test expection) to text labels.
    #      key   is (result, expect, random)
    #      value is (tinderbox label, dev test category)
    LABELS = {
        (TestResult.CRASH, False, False): ('TEST-UNEXPECTED-FAIL', 'REGRESSIONS'),
        (TestResult.CRASH, False, True):  ('TEST-UNEXPECTED-FAIL', 'REGRESSIONS'),
        (TestResult.CRASH, True, False): ('TEST-UNEXPECTED-FAIL', 'REGRESSIONS'),
        (TestResult.CRASH, True, True):  ('TEST-UNEXPECTED-FAIL', 'REGRESSIONS'),

        (TestResult.FAIL, False, False): ('TEST-KNOWN-FAIL', ''),
        (TestResult.FAIL, False, True):  ('TEST-KNOWN-FAIL (EXPECTED RANDOM)', ''),
        (TestResult.FAIL, True, False): ('TEST-UNEXPECTED-FAIL', 'REGRESSIONS'),
        (TestResult.FAIL, True, True):  ('TEST-KNOWN-FAIL (EXPECTED RANDOM)', ''),

        (TestResult.PASS, False, False): ('TEST-UNEXPECTED-PASS', 'FIXES'),
        (TestResult.PASS, False, True):  ('TEST-PASS (EXPECTED RANDOM)', ''),
        (TestResult.PASS, True, False): ('TEST-PASS', ''),
        (TestResult.PASS, True, True):  ('TEST-PASS (EXPECTED RANDOM)', ''),
        }

    def list(self, options):
        for label, paths in sorted(self.groups.items()):
            if label == '': continue

            print label
            for path in paths:
                print '    %s' % path

        if options.failure_file:
              failure_file = open(options.failure_file, 'w')
              if not self.all_passed():
                  for path in self.groups['REGRESSIONS']:
                      print >> failure_file, path
              failure_file.close()

        suffix = '' if self.finished else ' (partial run -- interrupted by user)'
        if self.all_passed():
            print 'PASS' + suffix
        else:
            print 'FAIL' + suffix

    def all_passed(self):
        return 'REGRESSIONS' not in self.groups

def run_tests(options, tests, results):
    """Run the given tests, sending raw results to the given results accumulator."""
    pb = None
    if not options.hide_progress:
        try:
            from mozillaJSTestSuite.progressbar import ProgressBar
            pb = ProgressBar('', len(tests), 16)
        except ImportError:
            pass
    results.pb = pb

    test_list = [ TestTask(test, options) for test in tests ]
    pipeline = Source(test_list, results, False)
    results.finished = pipeline.start(options.worker_count, options)

    if pb: 
        pb.finish()

    if not options.tinderbox:
        results.list(options)

def main(testCasesDirectory,targetDirectory,js_shell_path=None, createFragPool=False):        
    from optparse import OptionParser
    op = OptionParser(usage='%prog JS_SHELL [TEST-SPECS]')
    op.add_option('-s', '--show-cmd', dest='show_cmd', action='store_true',
                  help='show js shell command run')
    op.add_option('-o', '--show-output', dest='show_output', action='store_true',
                  help='show output from js shell')
    op.add_option('-O', '--output-file', dest='output_file',
                  help='write command output to the given file')
    op.add_option('-f', '--file', dest='test_file', action='append',
                  help='get tests from the given file')
    op.add_option('-x', '--exclude-file', dest='exclude_file', action='append',
                  help='exclude tests from the given file')
    op.add_option('--no-progress', dest='hide_progress', action='store_true',
                  help='hide progress bar')
    op.add_option('-j', '--worker-count', dest='worker_count', type=int, default=2,
                  help='number of worker threads to run tests on (default 2)')
    op.add_option('-m', '--manifest', dest='manifest',
                  help='select manifest file')
    op.add_option('-t', '--timeout', dest='timeout', type=float, default=150.0,
                  help='set test timeout in seconds')
    op.add_option('-d', '--exclude-random', dest='random', action='store_false',
                  help='exclude tests marked random', default=True)
    op.add_option('--run-skipped', dest='run_skipped', action='store_true',
                  help='run skipped tests')
    op.add_option('--run-only-skipped', dest='run_only_skipped', action='store_true',
                  help='run only skipped tests')
    op.add_option('--tinderbox', dest='tinderbox', action='store_true',
                  help='Tinderbox-parseable output format')
    op.add_option('--args', dest='shell_args', default='',
                  help='extra args to pass to the JS shell')
    op.add_option('-g', '--debug', dest='debug', action='store_true',
                  help='run test in debugger')
    op.add_option('--valgrind', dest='valgrind', action='store_true',
                  help='run tests in valgrind')
    op.add_option('--valgrind-args', dest='valgrind_args',
                  help='extra args to pass to valgrind')
    op.add_option('-c', '--check-manifest', dest='check_manifest', action='store_true',
                  help='check for test files not listed in the manifest')
    op.add_option('--failure-file', dest='failure_file',
                  help='write tests that have not passed to the given file')
    op.add_option('--run-slow-tests', dest='run_slow_tests', action='store_true',
                  help='run particularly slow tests as well as average-speed tests')
    op.add_option('--xul-info', dest='xul_info_src',
                  help='config data for xulRuntime (avoids search for config/autoconf.mk)')
    op.add_option('--no-extensions', dest='no_extensions', action='store_true',
                  help='run only tests conforming to the ECMAScript 5 standard')
    (options, args) = op.parse_args()
    if len(args) < 1:
        if js_shell_path is not None:
            JS = js_shell_path
        else:
            print "No JS persistent Shell found."
            sys.exit()
    else:
        JS, args = args[0], args[1:]
    # Convert to an absolute path so we can run JS from a different directory.
    if JS is not None:
        JS = os.path.abspath(JS)
    
    if options.debug:
        if options.valgrind:
            print >> sys.stderr, "--debug and --valgrind options are mutually exclusive"
            sys.exit(2)
        debugger_prefix = ['gdb', '-q', '--args']
    elif options.valgrind:
        debugger_prefix = ['valgrind']
        if os.uname()[0] == 'Darwin':
            debugger_prefix.append('--dsymutil=yes')
        if options.valgrind_args:
            debugger_prefix.append(options.valgrind_args)
        # Running under valgrind is not very useful if we don't show results.
        options.show_output = True 
    else:
        debugger_prefix = []

    TestTask.set_js_cmd_prefix(JS, options.shell_args.split(), debugger_prefix)

    output_file = sys.stdout
    if options.output_file and (options.show_cmd or options.show_output):
        output_file = open(options.output_file, 'w')
    ResultsSink.output_file = output_file

    if ((options.show_cmd or options.show_output) and 
        output_file == sys.stdout or options.tinderbox):
        options.hide_progress = True

    if options.manifest is None:
        filename = os.path.join(os.path.dirname(__file__), 'mozillaJSTestSuite/jstests.list')
        if os.path.isfile(filename):
            options.manifest = filename
        else:
            print >> sys.stderr, 'no manifest file given and defaults not found'
            sys.exit(2)

    import mozillaJSTestSuite.manifest
    if JS is None:
        xul_tester = mozillaJSTestSuite.manifest.NullXULInfoTester()
    else:
        if options.xul_info_src is None:
            xul_info = mozillaJSTestSuite.manifest.XULInfo.create(JS)
        else:
            xul_abi, xul_os, xul_debug = options.xul_info_src.split(r':')
            xul_debug = xul_debug.lower() is 'true'
            xul_info = mozillaJSTestSuite.manifest.XULInfo(xul_abi, xul_os, xul_debug)
        xul_tester = mozillaJSTestSuite.manifest.XULInfoTester(xul_info, JS)
    test_list = mozillaJSTestSuite.manifest.parse(options.manifest, xul_tester)
    fileList=mozillaJSTestSuite.manifest.fileList
    
    processList=[]
    resultQueue=multiprocessing.Queue()
    codeFrags=defaultdict(dict)

    threads=False
    for f in fileList:
        if threads:
            a = AntlrParser(resultQueue)
            t=threading.Thread(target=a.extractCodeFrag,args=(None,f))
            processList.append(t)
        else:
            a = AntlrParser()
            d=a.extractCodeFrag(None,f)
            keys=codeFrags.keys()
            if d is not None:
                for nt in d.keys():
                    if nt not in keys:
                        codeFrags[nt]=d.get(nt)
                    else:
                        codeFrags.get(nt).update(d.get(nt))
                    

    processCount = len(processList)
    continueLoop=True
    s=0
    t=100
    
    while True and threads:
        if t > processCount:
            t=processCount
            continueLoop = False
        for i in range(s,t):
            processList[i].start()
        for i in range(s,t):
            processList[i].join(300)
        if not continueLoop:
            break
        s=t
        t=t+100
    
    
    print "Spandan1"
    print datetime.datetime.now()
    if threads:
        for i in range(resultQueue.qsize()):
            d=resultQueue.get()
            keys=codeFrags.keys()
            for nt in d.keys():
                    if nt not in keys:
                        codeFrags[nt]=d.get(nt)
                    else:
                        codeFrags.get(nt).update(d.get(nt))

                            
    for key in codeFrags.keys():
        print key
        print codeFrags.get(key)
    
    print "Spandan2"
    print datetime.datetime.now()
    
    if options.check_manifest:
        check_manifest(test_list)
        if JS is None:
            sys.exit()

    if options.test_file:
        paths = set()
        for test_file in options.test_file:
            paths |= set([ line.strip() for line in open(test_file).readlines()])
        test_list = [ _ for _ in test_list if _.path in paths ]

    if args:
        def p(path):
            for arg in args:
                if path.find(arg) != -1:
                    return True
            return False
        test_list = [ _ for _ in test_list if p(_.path) ]

    if options.exclude_file:
        test_list = exclude_tests(test_list, options.exclude_file)

    if options.no_extensions:
        test_list = [_ for _ in test_list if '/extensions/' not in _.path]

    if not options.random:
        test_list = [ _ for _ in test_list if not _.random ]

    if options.run_only_skipped:
        options.run_skipped = True
        test_list = [ _ for _ in test_list if not _.enable ]

    if not options.run_slow_tests:
        test_list = [ _ for _ in test_list if not _.slow ]

    if options.debug and test_list:
        if len(test_list) > 1:
            print('Multiple tests match command line arguments, debugger can only run one')
            for tc in test_list:
                print('    %s' % tc.path)
            sys.exit(2)

        cmd = test_list[0].get_command(TestTask.js_cmd_prefix)
        if options.show_cmd:
            print subprocess.list2cmdline(cmd)
        manifest_dir = os.path.dirname(options.manifest)
        if manifest_dir not in ('', '.'):
            os.chdir(os.path.dirname(options.manifest))
        call(cmd)
        sys.exit()

    if not test_list:
        print 'no tests selected'
    else:
        curdir = os.getcwd()
        manifest_dir = os.path.dirname(options.manifest)
        if manifest_dir not in ('', '.'):
            os.chdir(os.path.dirname(options.manifest))
        try:
            results = ResultsSink()
            #run_tests(options, test_list, results)
            while True:
                filename = os.path.join(os.path.dirname(__file__), "jstests_generated.list")
                runFuzzer(filename,testCasesDirectory,targetDirectory)
                if os.path.isfile(filename):
                    test_list=mozillaJSTestSuite.manifest.parse(filename, xul_tester, createFragPool)
                    #run_tests(options, test_list, results)
                
                break
            
        finally:
            os.chdir(curdir)

    if output_file != sys.stdout:
        output_file.close()

    if not results.all_passed():
        sys.exit(1)

