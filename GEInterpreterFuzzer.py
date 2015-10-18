#!/usr/bin/env python
from marshal import dump, load
from GECodeGenerator import runFuzzer 
from datetime import datetime
from string import lower
import sys
from os import listdir, mkdir, makedirs,remove,stat
from os.path import isfile, join, isdir, exists, abspath
from langparser.AntlrParser import *
from Queue import Queue
from collections import defaultdict
from shutil import copyfile, rmtree
import ConfigParser
import logging
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, )

testsuite=config.get('Testsuite', 'testsuitedirs').split(',')
targetDirectory=config.get('TargetDir', 'DIR')
tempDirectoryName=config.get('TargetDir', 'TEMP')
database=config.get('TargetDir', 'Database')

SHELL_FILES=config.get('Interpreter', 'SHELL_FILES')
EXCLUDE_FILES = set(config.get('Exclude', 'FILES').split(','))
INCLUDE_NT=None

fileList = []
interpreters = {}
interpreterList=config.get('Interpreter', 'SHELL_PATH').split(';')
for i in interpreterList:
    splitValues=i.split(':')
    interpreters[splitValues[0]]=splitValues[1].split(',')
shell=interpreters.keys()
options=interpreters.values()

def listAllTestCases(testCasesDir):
    if(isinstance(testCasesDir,list)):
        for dir in testCasesDir:
            listAllTestCasesDir(dir)
    else:
        listAllTestCasesDir(testCasesDir)

def listAllTestCasesDir(testCaseDir):
    for f in listdir(testCaseDir):
            fi=join(testCaseDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
                if f.endswith("js") and f not in EXCLUDE_FILES:
                    fileList.append(abspath(fi))

def createFragmentPool():
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
            listAllTestCases(testsuite)
            if input1=='y':
                raw_input("Updating Existing Fragment Pool\n Press any key to continue...")
                moveFiles(1)
            else:
                raw_input("Deleting Existing Fragment Pool\n Press any key to continue...")
                if exists(tempDirectoryName):
                    rmtree(tempDirectoryName)
                moveFiles(0)
                fileList[:] = []
                listAllTestCases(tempDirectoryName)
                for f in fileList1:
                    remove(database+"/"+f)
            break;
        else:
            print "Answer must be 'Y' or 'N'"
    codeFragPool=[]
    print("Considering " + str(len(fileList)) + " files for learning code fragments " + str(datetime.now()))
    if not exists(database):
        makedirs(database)
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

def moveFiles(update = 0):
    try:
        if not exists(tempDirectoryName):
            makedirs(tempDirectoryName)
        if not exists(targetDirectory):
            makedirs(targetDirectory)
        if len(listdir(tempDirectoryName)) == 0 or update==1:
            count=len(listdir(tempDirectoryName))
            for f in fileList:
                statinfo=stat(f)
                if statinfo.st_size == 0:
                    continue
                from subprocess import Popen,PIPE
                #interpreter defined code-starts
                exec_cmd="timeout 3 "+ shell[0] + " -f " + SHELL_FILES + " " + f
                p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
                (out0,err0)=p.communicate()
                rc0= p.returncode
                exec_cmd="timeout 3 "+ shell[1] +" " + SHELL_FILES + " " + f
                p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
                (out1,err1)=p.communicate()
                rc1= p.returncode
                if rc1 == 1 or rc0==3:
                    continue
                #interpreter defined code-ends
                newfname=tempDirectoryName+"/"+str(count)+".js"
                count+=1
                copyfile(f, newfname)
            print "Copied " + str(count) + " files to temporary location"
    except:
        pass

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.setrecursionlimit(300000)
    if args[0]=="0":
        createFragmentPool()
    listAllTestCases(testsuite)
    moveFiles(0)
    from GECodeGenerator import runFuzzer         
    runFuzzer(targetDirectory,shell,options,EXCLUDE_FILES,INCLUDE_NT,SHELL_FILES)