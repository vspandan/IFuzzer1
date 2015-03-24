#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
from datetime import datetime
import os
from string import lower
import sys
from random import choice

JS_SHELL_PATH1="/home/spandan/mozilla/js-1.8.5/js/src/dist/bin/js"
JS_SHELL_PATH2="/home/spandan/mozilla/centralrepo/mozilla-central/js/src/dist/bin/js"

CrashListFile1="CrashList1"
TypeErrorList1="TypeErrorList1"
CrashListFile2="CrashList2"
TypeErrorList2="TypeErrorList2"


TargetDirectory =  "generatedTestCases"
TestCasesDirectory= "testsamples"

CREATE_FRAG_POOL=False
GEN_PRGS=True
GUI=False
EXCLUDE_FILES = set(('browser.js', 'shell.js', 'jsref.js', 'template.js',
                    'user.js', 'sta.js',
                    'test262-browser.js', 'test262-shell.js',
                    'test402-browser.js', 'test402-shell.js',
                    'testBuiltInObject.js', 'testIntl.js',
                    'js-test-driver-begin.js', 'js-test-driver-end.js','gcstats.js','os.js'))

INCLUDE_NT=['block','ifStatement','iterationStatement','continueStatement','withStatement','switchStatement','throwStatement','tryStatement','catchProduction','initialiser','functionDeclaration','functionExpression','assignmentOperator','booleanLiteral','numericLiteral','literal','caseClause','expressionSequence','singleExpression']

def options(choice):
    if choice == 1:
        return lower(raw_input("Do you want to Append Fragment Pool ? Y/N : "))
    else:
        return lower(raw_input("Do you want to create fragment pool ? Y/N : "))

if __name__ == "__main__":
    try:
        sys.setrecursionlimit(100000)
        print datetime.now()
        if not os.path.isdir(TargetDirectory):
            os.mkdir(TargetDirectory)
        if not os.path.isdir("database"):
            os.mkdir("database")
        if not os.path.exists(TargetDirectory+"/shell.js"):
            f=open(TargetDirectory+"/shell.js","a+")
            f.close()
        while True:
            input=options(0)
            if input in ['y','n']:
                if input=='y':
                    CREATE_FRAG_POOL=True

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

                    
                break;
            else:
                 print "Answer must be 'Y' or 'N'"
        
        #JS_SHELL_OPTIONS=["  -f"]
        #main(TestCasesDirectory,TargetDirectory,CrashListFile1,TypeErrorList1,JS_SHELL_OPTIONS,JS_SHELL_PATH1,GUI,GEN_PRGS,CREATE_FRAG_POOL,EXCLUDE_FILES,INCLUDE_NT)


        JS_SHELL_OPTIONS=[' --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --thread-count=2 --fuzzing-safe  -f', ' --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --no-fpu --thread-count=2 --fuzzing-safe  -f', ' --no-baseline --no-ion --thread-count=2 --fuzzing-safe  -f', ' --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-threads --fuzzing-safe  -f', ' --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-fpu --no-threads --fuzzing-safe  -f', ' --no-baseline --no-ion --no-threads --fuzzing-safe  -f']
        main(TestCasesDirectory,TargetDirectory,CrashListFile2,TypeErrorList2,JS_SHELL_OPTIONS,JS_SHELL_PATH2,GUI,GEN_PRGS,CREATE_FRAG_POOL,EXCLUDE_FILES,INCLUDE_NT)
        
        print datetime.now()
    except:
        pass       
