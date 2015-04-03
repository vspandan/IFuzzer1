#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from datetime import datetime
from string import lower
import sys
from random import choice
from os import listdir, mkdir, makedirs
from os.path import isfile, join, isdir, exists, abspath

JS_SHELL_PATH1="/home/spandan/mozilla/js-1.8.5/js/src/dist/bin/js"
JS_SHELL_PATH2="/home/spandan/mozilla/centralrepo/mozilla-central/js/src/dist/bin/js"

JS_SHELL_OPTIONS1=[' -w -f ', ' -w -Z 1 -f',' -w -Z 0 -f', ' -w -j -f',' -w -m -f',' -w -p -f',' -w -m -a -f']
JS_SHELL_OPTIONS2=[' --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f',         ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --thread-count=2 --fuzzing-safe  -f', ' --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --no-fpu --thread-count=2 --fuzzing-safe  -f', ' --no-baseline --no-ion --thread-count=2 --fuzzing-safe  -f', ' --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-threads --fuzzing-safe  -f', ' --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-fpu --no-threads --fuzzing-safe  -f', ' --no-baseline --no-ion --no-threads --fuzzing-safe  -f']

targetDirectory="testsamples/tests_67eac0234f15"
targetDirectoryName="generatedTestCases_js31_"

CrashListFile1="CrashList1"
TypeErrorList1="TypeErrorList1"
CrashListFile2="CrashList2"
TypeErrorList2="TypeErrorList2"

GUI=False
EXCLUDE_FILES = set(('browser.js', 'shell.js', 'jsref.js', 'template.js', 'user.js', 'sta.js','test262-browser.js', 'test262-shell.js','test402-browser.js', 'test402-shell.js', 'testBuiltInObject.js', 'testIntl.js','js-test-driver-begin.js', 'js-test-driver-end.js','gcstats.js','os.js'))

INCLUDE_NT=['block','ifStatement','iterationStatement','withStatement','labelledStatement','expressionSequence','switchStatement','throwStatement','tryStatement','catchProduction','functionDeclaration','arrayLiteral','objectLiteral','propertyNameAndValueList','functionExpression','assignmentOperator','propertyName','numericLiteral','literal','singleExpression']

fileList = []

def options(choice):
    if choice == 1:
        return lower(raw_input("Do you want to Append Fragment Pool ? Y/N : "))
    else:
        return lower(raw_input("Do you want to create fragment pool ? Y/N : "))

def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
                if f.endswith("js") and f not in EXCLUDE_FILES:
                    fileList.append(fi)

def createFragmentPool():
    codeFragPool=[]
    def finalize():
        codeFrags2=defaultdict(list)
        print (datetime.datetime.now())
        print ("Finalizing: Grouping Common Frags")
        for codeFrags in codeFragPool:
            keys=codeFrags2.keys()
            for key in codeFrags.keys():
                if key in keys:
                    codeFrags2[key] = codeFrags2.get(key)+codeFrags.get(key)
                else:
                    codeFrags2[key]=codeFrags.get(key)
        print (datetime.datetime.now())
        print ("Finalizing: Writing to file")
        for key in codeFrags2.keys():
            print (key)
            fileName = "database" + "/" + key
            temp=[]
            if isfile(fileName):
                f2 = open(fileName, 'rb')
                temp=load(f2)
                f2.close()
            if temp is None:
                temp = list(codeFrags2.get(key))
            else:
                temp = temp+list(codeFrags2.get(key))
            f1 = open(fileName, 'wb')
            dump(temp, f1)
            f1.close()
            print (datetime.datetime.now())
        
    print("Considering " + str(len(fileList)) + " files for learning code fragments")
    if not exists("database"):
        makedirs("database")
    count=0
    a=AntlrParser(que)
    for f in fileList:
        try:
            que=Queue.Queue()
            a.que=que
            t=threading.Thread(target=a.extractCodeFrag,kwargs={'fileName':f})
            t.start()
            t.join(90)
            timeout=False
            if t.isAlive():
                try:
                    timeout=True
                    raise TimeLimitExpired()
                except:
                    #print "killed"
                    continue
            if not timeout:
                res=que.get(False)
                if res is not None:
                    codeFragPool.append(res)
                    count+=1
            
            if count % 200 == 0:
                finalize()
                codeFragPool=[]
        except:
            pass

    finalize()
    print ("Finished; Code generation and testing begins")

def main(fileList):
    iteration=0
    targetDirectory=targetDirectoryName
    try:
        while True:
            if not isdir(targetDirectory):
                mkdir(targetDirectory)
            if not exists(targetDirectory+"/shell.js"):
                f=open(targetDirectory+"/shell.js","a+")
                f.close()
            if GUI:
                from GECodeGeneratorGUI import runFuzzer 
            else:
                from GECodeGenerator import runFuzzer 
            generatedFileList=runFuzzer(fileList,targetDirectory, JS_SHELL_PATH2,JS_SHELL_OPTIONS2,EXCLUDE_FILES,INCLUDE_NT)
            fileList=generatedFileList
            targetDirectory=targetDirectoryName+str(iteration)
            iteration+=1
    except:
        pass

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    print "Starting Application "
    print datetime.now()
    listAllTestCasesDir(targetDirectory)
    while True:
        input=options(0)
        if input in ['y','n']:
            if input=='y':
                fileList=os.listdir("database")
                if len(fileList):
                    while True:
                        input1=options(1)
                        if input1 in ['y','n']:
                            if input1=='y':
                                raw_input("Updating Existing Fragment Pool\n Press any key to continue...")
                                break;
                            else:
                                raw_input("Deleting Existing Fragment Pool\n Press any key to continue...")
                                for f in fileList:
                                    os.remove("database"+"/"+f)
                                break;

                        else:
                            print "Answer must be 'Y' or 'N'"
                createFragmentPool()
                break;
            else:
                break;
        else:
             print "Answer must be 'Y' or 'N'"
    main(fileList)
              
