#!/usr/bin/env python
from marshal import dump
from subprocess import Popen,PIPE
from string import lower
from threading import Thread
from os import listdir, mkdir, makedirs,remove,stat,kill
from os.path import isfile, join, isdir, exists, abspath
from Queue import Queue
from shutil import copyfile, rmtree
from GECodeGenerator import GECodeGenerator
from time import sleep
import sys
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

testsuite=config.get('Testsuite', 'TESTSUITE').split(',')

FILE_TYPE = config.get('Interpreter', 'FILE_TYPE')
LIB_FILE = config.get('Interpreter', 'LIB_FILE')
FILELISTFILE= abspath(config.get('TargetDir', 'FILELIST'))
INCLUDE_NT = config.get('Interpreter', 'SELECTEDNT').split(",")

INCLUDE_NT1 = None

fileList = []
libfiLes=[]
shellfileOption = []

shell=config.get('Interpreter', 'SHELL_PATH').split(',')
options=(config.get('Interpreter', 'SHELL_OPTIONS').split(','))
returnCodes=[]
for code in config.get('Interpreter', 'SHELL_RETURN_CODES').split(','):
    returnCodes.append(int(code))
fileOptionSpecifier=config.get('Interpreter', 'SHELL_FILE_SPECIFIER').strip()
    

"""
Lists all the directories and makes a call to list the files
"""
def listAllTestCases(testCasesDir):
    if(isinstance(testCasesDir,list)):
        for dir in testCasesDir:
            listAllTestCasesDir(dir)
    else:
        listAllTestCasesDir(testCasesDir)

"""
Lists all the files in a directory
"""
def listAllTestCasesDir(testCaseDir):
    for f in listdir(testCaseDir):
            fi=join(testCaseDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
                if f.endswith(FILE_TYPE):
                    fileList.append(abspath(fi))
                    if f.endswith(LIB_FILE):
                        statinfo=stat(abspath(fi))
                        if statinfo.st_size == 0:
                            continue
                        libfiLes.append(abspath(fi))

def run_cmd(fi,l,option,shellNum):
    try:
        cmd=[]
        cmd.append(shell[shellNum].strip())
        cmd=cmd+option.split()
        if len(shellfileOption)>0:
            cmd=cmd+shellfileOption[shellNum]
        cmd.append(fi)
        p = Popen(cmd, stdout=PIPE,stderr=PIPE)
        l[0]=p
        out, err = p.communicate()
        l[1]=(out,err,p.returncode)
        sys.stdout.flush()
        sys.stderr.flush()
    except Exception as e:
        print e
        pass

"""
Elimiates unwanted files
"""
def collectFiles():
    try:
        tempList = []
        print "Total Number of Files "+ str(len(fileList))
        for f in fileList:
            statinfo=stat(f)
            if statinfo.st_size == 0:
                continue
            print f
            from subprocess import Popen,PIPE
            flag=True
            for a in range(len(shell)):
                try:
                    l=[None,None]
                    t=Thread(target=run_cmd,kwargs={'fi':f,'l':l,'option':options[0],'shellNum':a})
                    t.start()
                    t.join(3)
                    if t.isAlive():
                        if l[0] is not None:
                            l[0].kill()
                            kill(l[0].pid, 9)
                            sleep(.1)
                    (out0,err0,rc0)=l[1]
                    if rc0 == returnCodes[1]:
                        print err0
                        flag=False
                        break
                except Exception as e:
                    print(e)
            if flag:   
                tempList.append(f)
        print "Files Listed for Processing "+ str(len(tempList))
        fileList[:] =tempList
        f1 = open(FILELISTFILE, 'wb')
        dump(fileList,f1)
        f1.close()
    finally:
        pass

"""
Driver function
"""
if __name__ == "__main__":
    args = sys.argv[1:]
    sys.setrecursionlimit(300000)
    listAllTestCases(testsuite)
    g=GECodeGenerator()
    for a in range(len(shell)):
        shellfileoption=[]
        for shellfile in libfiLes:
            shellfileoption.append(shellfile)
            if len(fileOptionSpecifier)>0:
                shellfileoption.append(fileOptionSpecifier)
        shellfileOption.append(shellfileoption)
    if args[0]=="0":
        if exists(FILELISTFILE):
            remove(FILELISTFILE)
        collectFiles()
        g.genFragPool()
    if not exists(FILELISTFILE):
        collectFiles()
    g.runFuzzer(shell,options,returnCodes,INCLUDE_NT,shellfileOption)