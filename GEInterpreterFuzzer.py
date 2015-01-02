#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
from datetime import datetime
import os
from string import lower
import sys

JS_SHELL_PATH="/home/spandan/js-1.8.5/js/src/dist/bin/js"
CREATE_FRAG_POOL=False
TargetDirectory =  "../generatedTestCases"
TestCasesDirectory= "../testsamples"
FragPoolDirName="database"
FragPool= "../"+FragPoolDirName


def options(choice):
    if choice == 1:
        return lower(raw_input("Do you want to Append Fragment Pool ? Y/N : "))
    else:
        return lower(raw_input("Do you want to create fragment pool ? Y/N : "))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    print datetime.now()
    
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
        
    main(TestCasesDirectory,TargetDirectory,JS_SHELL_PATH,CREATE_FRAG_POOL)
    print datetime.now()
 