#!/usr/bin/env python
from marshal import dump
from string import lower
from os import listdir, mkdir, makedirs,remove,stat
from os.path import isfile, join, isdir, exists, abspath
from Queue import Queue
from shutil import copyfile, rmtree
from GECodeGenerator import GECodeGenerator
import sys
import ConfigParser
import logging

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
LOG_FILENAME= config.get('Mappings', 'mappings.logfile')
LOG_LEVEL= config.get('Mappings', 'loglevel');
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, )

testsuite=config.get('Testsuite', 'TESTSUITE').split(',')

FILE_TYPE = config.get('Interpreter', 'FILE_TYPE')
LIB_FILE = config.get('Interpreter', 'LIB_FILE')
FILELISTFILE= abspath(config.get('TargetDir', 'FILELIST'))
INCLUDE_NT = None

fileList = []
shell=[]
options=[]
returnCodes=[]
libfiLes=[]
fileOptionSpecifier=[]
shellfileOption = []

"""
Initializes the options
"""
def generateOptions():
    for i in config.get('Interpreter', 'SHELL_PATH').split('||'):
        splitValues=i.split(':')
        shell.append(splitValues[0])
        options.append(splitValues[1].split(','))
        returncode=[]
        for j in splitValues[2].split(','):
            returncode.append(int(j))
        returnCodes.append(returncode)
        fileOptionSpecifier.append(splitValues[3].strip())

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
                cmd=['timeout','5']
                cmd.append(shell[a])
                option=options[a][0].strip();
                if len(option)>0:
                    cmd=cmd+option.split()
                if len(shellfileOption[a])>0:
                    cmd=cmd+shellfileOption[a]
                cmd.append(f)
                p = Popen(cmd, stdout=PIPE,stderr=PIPE)
                (out0,err0) = p.communicate()
                rc0 = p.returncode
                if rc0 == returnCodes[a][1]:
                    print err0
                    flag=False
                    break
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
    generateOptions()
    g=GECodeGenerator()
    if args[0]=="0":
        g.genFragPool(fileList)
    for a in range(len(shell)):
        shellfileoption=[]
        for shellfile in libfiLes:
            shellfileoption.append(shellfile)
            if len(fileOptionSpecifier[a])>0:
                shellfileoption.append(fileOptionSpecifier[a])
        shellfileOption.append(shellfileoption)
    if not exists(FILELISTFILE):
        collectFiles()
    g.runFuzzer(shell,options,returnCodes,INCLUDE_NT,shellfileOption)