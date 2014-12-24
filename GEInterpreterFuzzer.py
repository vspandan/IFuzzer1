#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
from datetime import datetime
import os
from string import lower

JS_SHELL_PATH="/home/spandan/js-1.8.5/js/src/dist/bin/js"
CREATE_FRAG_POOL=False
TargetDirectory = os.path.join(os.path.dirname(__file__), "generatedTestCases")
TestCasesDirectory=os.path.join(os.path.dirname(__file__), "testsamples")

def options():
    return lower(raw_input("Do you want to create fragment pool (Default: No)? Y/N"))

if __name__ == "__main__":
    print datetime.now()
    
    while True:
        input=options()
        if input in ['y','n']:
            if input=='y':
                CREATE_FRAG_POOL=True
            break;
        else:
             print "Answer must be 'Y' or 'N'"
        
    main(TestCasesDirectory,TargetDirectory,JS_SHELL_PATH,CREATE_FRAG_POOL)
    print datetime.now()
 