#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
from datetime import datetime
import os

JS_SHELL_PATH="/home/spandan/js-1.8.5/js/src/dist/bin/js"
CREATE_FRAG_POOL=False
TargetDirectory = os.path.join(os.path.dirname(__file__), "generatedTestCases")
TestCasesDirectory=os.path.join(os.path.dirname(__file__), "testsamples")
if __name__ == "__main__":
    print datetime.now()
    main(TestCasesDirectory,TargetDirectory,JS_SHELL_PATH,CREATE_FRAG_POOL)
    print datetime.now()
 