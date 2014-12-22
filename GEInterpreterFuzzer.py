#!/usr/bin/env python

from GECodeGenerator import runFuzzer 
from JSDriver import main
import threading

JS_SHELL_PATH="/home/spandan/js-1.8.5/js/src/dist/bin/js"
CREATE_FRAG_POOL=False

if __name__ == "__main__":
    mainThread=threading.Thread(name="Persistent Shell",target= main(JS_SHELL_PATH,CREATE_FRAG_POOL))
    mainThread.start()
    mainThread.join()
 