#!/usr/bin/env python
from marshal import dump, load
from GECodeGenerator import runFuzzer 
from datetime import datetime
from string import lower
import sys
from os import listdir, mkdir, makedirs,remove
from os.path import isfile, join, isdir, exists, abspath
from langparser.AntlrParser import AntlrParser
from Queue import Queue
from collections import defaultdict
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
import logging
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    )


JS_SHELL_PATH1="/home/spandan/mozilla/js-1.8.5/js/src/dist/bin/js"
JS_SHELL_PATH2="/home/spandan/mozilla/centralrepo/mozilla-central/js/src/dist/bin/js"
JS_SHELL_PATH3="/home/spandan/google/v8/out/native/shell"

JS_SHELL_OPTIONS1=[' -w -f ']
# JS_SHELL_OPTIONS1=[' -w -f ', ' -w -Z 1 -f',' -w -Z 0 -f', ' -w -j -f',' -w -m -f',' -w -p -f',' -w -m -a -f']
JS_SHELL_OPTIONS2=[' -w --fuzzing-safe  -f']
JS_SHELL_OPTIONS2=[' --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f',         ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --thread-count=2 --fuzzing-safe  -f', ' --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --no-fpu --thread-count=2 --fuzzing-safe  -f', ' --no-baseline --no-ion --thread-count=2 --fuzzing-safe  -f', ' --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-threads --fuzzing-safe  -f', ' --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-fpu --no-threads --fuzzing-safe  -f', ' --no-baseline --no-ion --no-threads --fuzzing-safe  -f']
JS_SHELL_OPTIONS3=None

testsuite="testsamples"
targetDirectoryName1="generatedTestCases_js18_"
targetDirectoryName3="generatedTestCases_v8_"
targetDirectoryName2="generatedTestCases_js31_"

CrashListFile1="CrashList1"
TypeErrorList1="TypeErrorList1"
CrashListFile2="CrashList2"
TypeErrorList2="TypeErrorList2"

GUI=False
EXCLUDE_FILES = set(('browser.js', 'shell.js', 'jsref.js', 'template.js', 'user.js', 'sta.js','test262-browser.js', 'test262-shell.js','test402-browser.js', 'test402-shell.js', 'testBuiltInObject.js', 'testIntl.js','js-test-driver-begin.js', 'js-test-driver-end.js','gcstats.js','js'))

INCLUDE_NT=['primaryExpression','ifStatement', 'iterationStatement', 'labelledStatement', 'throwStatement', 'functionDeclaration', 'arrayLiteral', 'propertyAssignment', 'propertyName', 'assignmentExpression', 'conditionalExpression', 'logicalORExpression', 'logicalANDExpression', 'bitwiseORExpression', 'bitwiseXORExpression', 'bitwiseANDExpression', 'equalityExpression', 'relationalExpression', 'shiftExpression', 'additiveExpression', 'multiplicativeExpression', 'unaryExpression', 'postfixExpression', 'callExpression', 'functionExpression', 'assignmentOperator', 'literal', 'numericLiteral']

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
        logging.info (datetime.now())
        logging.info ("Finalizing: Grouping Common Frags")
        for codeFrags in codeFragPool:
            keys=codeFrags2.keys()
            for key in codeFrags.keys():
                if key in keys:
                    codeFrags2[key] = codeFrags2.get(key)+codeFrags.get(key)
                else:
                    codeFrags2[key]=codeFrags.get(key)
        logging.info (datetime.now())
        logging.info ("Finalizing: Writing to file")
        for key in codeFrags2.keys():
            logging.info (key)
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
            logging.info (datetime.now())
        
    logging.info("Considering " + str(len(fileList)) + " files for learning code fragments")
    if not exists("database"):
        makedirs("database")
    count=0
    ind=True
    for f in fileList:
        logging.info (count)
        if count > -1 :
            try:
                a=AntlrParser()
                que=Queue()
                a.que=que
                import threading
                t=threading.Thread(target=a.extractCodeFrag,kwargs={'fileName':f})
                t.start()
                t.join(10)
                timeout=False
                if t.isAlive():
                    try:
                        timeout=True
                        raise Exception('','')
                    except:
                        continue
                        a=None
                if not timeout:
                    res=que.get(False)
                    if res is not None:
                        codeFragPool.append(res)
                        logging.debug(res)
                
                if count % 200 == 0:
                    finalize()
                    codeFragPool=[]
            except:
                pass
        count+=1
    finalize()
    
    logging.info ("Finished; Code generation and testing begins")

def main(fileList,args):
    iteration=0
    try:
        while True:
            if GUI:
                from GECodeGeneratorGUI import runFuzzer 
            else:
                from GECodeGenerator import runFuzzer 
            if args[0] == '1':
                targetDirectory=targetDirectoryName1+str(iteration)
                if not isdir(targetDirectory):
                    mkdir(targetDirectory)
                # if not exists(targetDirectory+"/shell.js"):
                #     f=open(targetDirectory+"/shell.js","a+")
                #     f.close()
                generatedFileList=runFuzzer(fileList,targetDirectory, JS_SHELL_PATH1,JS_SHELL_OPTIONS1,EXCLUDE_FILES,INCLUDE_NT,1)
            elif args[0] == '2':
                targetDirectory=targetDirectoryName2+str(iteration)
                if not isdir(targetDirectory):
                    mkdir(targetDirectory)
                generatedFileList=runFuzzer(fileList,targetDirectory, JS_SHELL_PATH2,JS_SHELL_OPTIONS2,EXCLUDE_FILES,INCLUDE_NT,2)
            elif args[0] == '3':
                targetDirectory=targetDirectoryName3+str(iteration)
                if not isdir(targetDirectory):
                    mkdir(targetDirectory)
                generatedFileList=runFuzzer(fileList,targetDirectory, JS_SHELL_PATH3,JS_SHELL_OPTIONS3,EXCLUDE_FILES,INCLUDE_NT,3)
            else:
                print "Invalid Python Arguments"
            fileList=generatedFileList
            
            iteration+=1
    except:
        pass

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.setrecursionlimit(300000)
    print "Starting Application "
    logging.info (datetime.now())

    listAllTestCasesDir(testsuite)
    if args[0]=="0":
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
              
