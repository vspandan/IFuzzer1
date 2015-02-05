#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
from datetime import datetime
import os
from string import lower
import sys

JS_SHELL_PATH="/home/spandan/Desktop/js_03f3c7efaa5e/src/shell/js"
JS_SHELL_PATH1="/home/spandan/js-1.7.0/js/src/Linux_All_DBG.OBJ/js"
JS_SHELL_PATH2="/home/spandan/js-1.8.0/src/Linux_All_DBG.OBJ/js"
JS_SHELL_PATH3="/home/spandan/js-1.8.5/js/src/dist/bin/js"
JS_SHELL_PATH4="/home/spandan/js-17.0.0/js/src/shell/js17"
JS_SHELL_PATH5="/home/spandan/js-24.2.0/js/src/shell/js24"
JS_SHELL_PATH6="/home/spandan/js-31.2.0/js/src/js/src/shell/js"
CREATE_FRAG_POOL=False
TargetDirectory =  "generatedTestCases"
TestCasesDirectory= "testsamples"
FragPoolDirName="database"
CrashListFile="CrashList"
TypeErrorList="TypeErrorList"
CrashListFile1="CrashList1"
TypeErrorList1="TypeErrorList1"
CrashListFile2="CrashList2"
TypeErrorList2="TypeErrorList2"
CrashListFile3="CrashList3"
TypeErrorList3="TypeErrorList3"
CrashListFile4="CrashList4"
TypeErrorList4="TypeErrorList4"
CrashListFile5="CrashList5"
TypeErrorList5="TypeErrorList5"
CrashListFile6="CrashList6"
TypeErrorList6="TypeErrorList6"

def options(choice):
    if choice == 1:
        return lower(raw_input("Do you want to Append Fragment Pool ? Y/N : "))
    else:
        return lower(raw_input("Do you want to create fragment pool ? Y/N : "))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    print datetime.now()
    if not os.path.isdir(TargetDirectory):
        os.mkdir(TargetDirectory)
    if not os.path.isdir(FragPoolDirName):
        os.mkdir(FragPoolDirName)
    if not os.path.exists(TargetDirectory+"/shell.js"):
        f=open(TargetDirectory+"/shell.js","a+")
        f.close()
    while True:
        input=options(0)
        if input in ['y','n']:
            if input=='y':
                CREATE_FRAG_POOL=True

                fileList=os.listdir(FragPoolDirName)
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
                                    os.remove(FragPoolDirName+"/"+f)
                                break;
                        else:
                            print "Answer must be 'Y' or 'N'"

                
            break;
        else:
             print "Answer must be 'Y' or 'N'"
    
    #main(TestCasesDirectory,TargetDirectory,CrashListFile,TypeErrorList,JS_SHELL_PATH,CREATE_FRAG_POOL)
    #main(TestCasesDirectory,TargetDirectory,CrashListFile1,TypeErrorList1,JS_SHELL_PATH1,CREATE_FRAG_POOL)
    #main(TestCasesDirectory,TargetDirectory,CrashListFile2,TypeErrorList2,JS_SHELL_PATH2,CREATE_FRAG_POOL)
    main(TestCasesDirectory,TargetDirectory,CrashListFile3,TypeErrorList3,JS_SHELL_PATH3,CREATE_FRAG_POOL)
    #main(TestCasesDirectory,TargetDirectory,CrashListFile4,TypeErrorList4,JS_SHELL_PATH4,CREATE_FRAG_POOL)
    #main(TestCasesDirectory,TargetDirectory,CrashListFile5,TypeErrorList5,JS_SHELL_PATH5,CREATE_FRAG_POOL)
    #main(TestCasesDirectory,TargetDirectory,CrashListFile6,TypeErrorList6,JS_SHELL_PATH6,CREATE_FRAG_POOL)
    print datetime.now()
 