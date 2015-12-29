#!/usr/bin/env python
from marshal import dump, load
from GECodeGenerator import runFuzzer 
from datetime import datetime
from string import lower
from os import listdir, mkdir, makedirs,remove,stat
from os.path import isfile, join, isdir, exists, abspath
from langparser.AntlrParser import *
from Queue import Queue
from collections import defaultdict
from shutil import copyfile, rmtree
import sys
import ConfigParser
import logging

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
LOG_FILENAME= config.get('Mappings', 'mappings.logfile')
LOG_LEVEL= config.get('Mappings', 'loglevel');
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, )

testsuite=config.get('Testsuite', 'TESTSUITE').split(',')
database=config.get('TargetDir', 'DATABASE')

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
Creates fragment pool
"""
def createFragmentPool():
    """
    Sub function with limited scope; Dumps the code fragments generated
    """
    def finalize():
        codeFrags2=defaultdict(list)
        print (datetime.now())
        print ("Finalizing: Grouping Common Frags")
        for codeFrags in codeFragPool:
            keys=codeFrags2.keys()
            for key in codeFrags.keys():
                if key in keys:
                    codeFrags2[key] = codeFrags2.get(key)+codeFrags.get(key)
                else:
                    codeFrags2[key]=codeFrags.get(key)
        for key in codeFrags2.keys():
            fileName = abspath(database + "/" + key)
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
        print (datetime.now())
        print ("Finalized: Writing to file")
    
    if not exists(database):
        makedirs(database)
    fileList1=listdir(database)
    while True:
        input1=raw_input("Do you want to Append Fragment Pool ? Y/N : ")
        if input1 in ['y','n']:
            if input1=='y':
                raw_input("Updating Existing Fragment Pool\n Press any key to continue...")
            else:
                raw_input("Deleting Existing Fragment Pool\n Press any key to continue...")
                for f in fileList1:
                    remove(database+"/"+f)
            break;
        else:
            print "Answer must be 'Y' or 'N'"
    codeFragPool=[]
    
    count=1
    ind=True
    for f in fileList:
        statinfo=stat(f)
        if count > -1 and statinfo.st_size <= 10000:
            print (count)
            print (f)
            res=extractCodeFrag(f)
            if res is not None:
                codeFragPool.append(res)
            if count % 100 == 0:
                finalize()
                codeFragPool=[]
        count+=1
    finalize()
    print ("Finished; Code generation and testing begins " +str(datetime.now()))

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
    if args[0]=="0":
        createFragmentPool()
    for a in range(len(shell)):
        shellfileoption=[]
        for shellfile in libfiLes:
            shellfileoption.append(shellfile)
            if len(fileOptionSpecifier[a])>0:
                shellfileoption.append(fileOptionSpecifier[a])
        shellfileOption.append(shellfileoption)
    if not exists(FILELISTFILE):
        collectFiles()
    from GECodeGenerator import runFuzzer         
    runFuzzer(shell,options,returnCodes,INCLUDE_NT,shellfileOption)