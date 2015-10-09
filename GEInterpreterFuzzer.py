#!/usr/bin/env python
from marshal import dump, load
from GECodeGenerator import runFuzzer 
from datetime import datetime
from string import lower
import sys
from os import listdir, mkdir, makedirs,remove,stat
from os.path import isfile, join, isdir, exists, abspath
from langparser.AntlrParser import *
from Queue import Queue
from collections import defaultdict
from shutil import copyfile
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');

import logging
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, )


JS_SHELL_PATH2="/home/rubbernecker/jsengines/v8/out/native/d8 "
# JS_SHELL_OPTIONS2=[' --debug-code --expose-gc ']
JS_SHELL_OPTIONS2=[' --debug-code --expose-gc -e ', ' -e ']
# JS_SHELL_OPTIONS2=[' /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js ',' --gdbjit_full --use-strict --enable-slow-asserts --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --use-strict --enable-slow-asserts /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --use-strict --debug-code --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --use-strict --debug-code /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --use-strict --verify-heap --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --use-strict --verify-heap /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --enable-slow-asserts --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --enable-slow-asserts /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --debug-code --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --debug-code /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --verify-heap --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --gdbjit_full --verify-heap /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --enable-slow-asserts --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --enable-slow-asserts /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --debug-code --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --debug-code /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --verify-heap --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --use-strict --verify-heap /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --enable-slow-asserts --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --enable-slow-asserts /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --debug-code --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --debug-code /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --verify-heap --harmony /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js',' --verify-heap /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js']

JS_SHELL_PATH1="/home/rubbernecker/jsengines/firefox/js/src/dist/bin/js"
# JS_SHELL_OPTIONS1=[' --ion-eager --ion-offthread-compile=off --fuzzing-safe -f ', ' --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads --fuzzing-safe -f ', ' --baseline-eager --fuzzing-safe -f ' , ' --baseline-eager --no--fuzzing-safe -fpu --fuzzing-safe -f ', ' --no-baseline --fuzzing-safe -f ', ' --no-ion --fuzzing-safe -f ' ]
JS_SHELL_OPTIONS1=[' --ion-eager --ion-offthread-compile=off --fuzzing-safe -e ', ' --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads --fuzzing-safe -e ', ' --baseline-eager --fuzzing-safe -e ' , ' --baseline-eager --no-fpu --fuzzing-safe -e ', ' --no-baseline --fuzzing-safe -e ', ' --no-ion --fuzzing-safe -e ' ]
# JS_SHELL_OPTIONS1=[' /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js ','--ion-eager --ion-offthread-compile=off -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js','--ion-eager --ion-offthread-compile=off --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js','--baseline-eager -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js','--baseline-eager --no-fpu -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js','--no-baseline -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js','--no-ion -f /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/sta.js /home/rubbernecker/jsengines/v8/test/test262-es6/data/harness/assert.js /home/rubbernecker/jsengines/v8/test/test262-es6/harness-adapt.js']

# testsuite="/home/rubbernecker/jsengines/v8/test/test262-es6/data/test"
testsuite="tests/tests/"

targetDirectory="generated"

tempDirectoryName="tmp"

EXCLUDE_FILES = set(('browser.js', 'shell.js', 'jsref.js', 'template.js', 'user.js', 'sta.js','test262-browser.js', 'test262-shell.js','test402-browser.js', 'test402-shell.js', 'testBuiltInObject.js', 'testIntl.js','js-test-driver-begin.js', 'js-test-driver-end.js','gcstats.js','js'))

INCLUDE_NT=None

fileList = []

def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
                if f.endswith("js") and f not in EXCLUDE_FILES:
                    fileList.append(abspath(fi))

def createFragmentPool():
    codeFragPool=[]
    def finalize():
        codeFrags2=defaultdict(list)
        print (datetime.now())
        print ("Finalizing: Grouping Common Frags")
        for codeFrags in codeFragPool:
            keys=codeFrags2.keys()
            for key in codeFrags.keys():
                if key in keys:
                    codeFrags2[key] = codeFrags2.get(key)+codeFrags.get(key)
                else:
                    codeFrags2[key]=codeFrags.get(key)
        for key in codeFrags2.keys():
            fileName = abspath("database" + "/" + key)
            temp=[]
            if isfile(fileName):
                f2 = open(fileName, 'rb')
                temp=load(f2)
                f2.close()
            if temp is None:
                temp = list(codeFrags2.get(key))
            else:
                temp = set(temp+list(codeFrags2.get(key)))
                temp=list(temp)
            f1 = open(fileName, 'wb')
            dump(temp, f1)
            f1.close()
        print (datetime.now())
        print ("Finalized: Writing to file")
        
    print("Considering " + str(len(fileList)) + " files for learning code fragments " + str(datetime.now()))
    if not exists("database"):
        makedirs("database")
    count=1
    escapeFileList=[]
    escapeFile=open("escape.lst","r")
    for line in escapeFile:
        escapeFileList.append(line.strip())
    escapeFile.close()
    ind=True
    for f in fileList:
        statinfo=stat(f)
        if count > -1 and statinfo.st_size <= 10000 and f not in escapeFileList:
            print (count)
            print (f)
            res=extractCodeFrag(f)
            if res is not None:
                codeFragPool.append(res)
            if count % 100 == 0:
                finalize()
                codeFragPool=[]
        count+=1
    finalize()
    print ("Finished; Code generation and testing begins " +str(datetime.now()))

def main(fileList,args):
    try:
        status=False
        shell=[JS_SHELL_PATH1,JS_SHELL_PATH2]
        options=[JS_SHELL_OPTIONS1,JS_SHELL_OPTIONS2]
        fileList2=[]
        flag=False
        if not exists(tempDirectoryName):
            makedirs(tempDirectoryName)
        if not isdir(targetDirectory):
            mkdir(targetDirectory)
        if len(listdir(targetDirectory)) == 0:
            listAllTestCasesDir(testsuite)
        else:
            flag=True
            listAllTestCasesDir(targetDirectory)
        if len(listdir(tempDirectoryName)) == 0:
            logging.info(datetime.now())
            logging.info("Moving files that has to be processed to temporary location")
            count=0
            escapeFileList=[]
            escapeFile=open("escape.lst","r")
            for line in escapeFile:
                escapeFileList.append(line.strip())
            escapeFile.close()
            for f in fileList:
                if f in escapeFileList:
                    continue
                from subprocess import Popen,PIPE
                exec_cmd="timeout 3 "+ shell[0] + " " + f
                p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
                (out0,err0)=p.communicate()
                rc0= p.returncode
                exec_cmd="timeout 3 "+ shell[1] +" -f "+f
                p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
                (out1,err1)=p.communicate()
                rc1= p.returncode
                if rc1 == 1 or rc0 == 3:
                    print [rc0,rc1]
                    continue
                newfname=tempDirectoryName+"/"+str(count)+".js"
                count+=1
                copyfile(f, newfname)
                # if flag:
                #     remove(f)
                fileList2.append(newfname)
            logging.info("Moved files that has to be processed to temporary location")
        else:
            logging.info("Loading file list")
            fileList[:] = []
            listAllTestCasesDir(tempDirectoryName)
            fileList2=fileList[:]
        
        from GECodeGenerator import runFuzzer         
        if args[0]=="1":
            runFuzzer(fileList2,targetDirectory, shell,options,EXCLUDE_FILES,INCLUDE_NT,0)
        if args[0]=="2":
            runFuzzer(fileList2,targetDirectory, shell,options,EXCLUDE_FILES,INCLUDE_NT,1)
    finally:
        pass

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.setrecursionlimit(300000)
    if args[0]=="0":
        listAllTestCasesDir(testsuite)
        if not exists("database"):
            makedirs("database")
        fileList1=listdir("database")
        if len(fileList1):
            while True:
                input1=raw_input("Do you want to Append Fragment Pool ? Y/N : ")
                if input1 in ['y','n']:
                    if input1=='y':
                        raw_input("Updating Existing Fragment Pool\n Press any key to continue...")
                        break;
                    else:
                        raw_input("Deleting Existing Fragment Pool\n Press any key to continue...")
                        for f in fileList1:
                            remove("database"+"/"+f)
                        break;

                else:
                    print "Answer must be 'Y' or 'N'"
        createFragmentPool()
    else:
        main(fileList,args)
              
