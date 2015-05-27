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
from shutil import copyfile
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
LOG_FILENAME= config.get('Mappings', 'mappings.logfile');
LOG_LEVEL= config.get('Mappings', 'loglevel');

import logging
logging.basicConfig(filename=LOG_FILENAME, level=LOG_LEVEL, )


JS_SHELL_PATH1="/home/spandan/mozilla/js-1.8.5/js/src/dist/bin/js"
JS_SHELL_PATH2="/home/spandan/mozilla/centralrepo/mozilla-central/js/src/dist/bin/js"
JS_SHELL_PATH3="/home/spandan/google/v8/out/native/shell"

JS_SHELL_OPTIONS1=[' -w -f ']
# JS_SHELL_OPTIONS1=[' -w -f ', ' -w -Z 1 -f',' -w -Z 0 -f', ' -w -j -f',' -w -m -f',' -w -p -f',' -w -m -a -f']
JS_SHELL_OPTIONS2=[' -w --fuzzing-safe  -f']
JS_SHELL_OPTIONS2=[' --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f',         ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --thread-count=2 --fuzzing-safe  -f', ' --ion-offthread-compile=off --thread-count=2 --fuzzing-safe  -f', ' --ion-eager --thread-count=2 --fuzzing-safe  -f', ' --baseline-eager --no-fpu --thread-count=2 --fuzzing-safe  -f', ' --no-baseline --no-ion --thread-count=2 --fuzzing-safe  -f', ' --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --no-sse3 --no-threads --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-threads --fuzzing-safe  -f', ' --ion-offthread-compile=off --no-threads --fuzzing-safe  -f', ' --ion-eager --no-threads --fuzzing-safe  -f', ' --baseline-eager --no-fpu --no-threads --fuzzing-safe  -f', ' --no-baseline --no-ion --no-threads --fuzzing-safe  -f']
JS_SHELL_OPTIONS3=None

testsuite="testsamples"
targetDirectoryName1="generatedTestCases_js18_"
targetDirectoryName3="generatedTestCases_v8_"
targetDirectoryName2="generatedTestCases_js31_"


tmpDirectoryName="tmp"

EXCLUDE_FILES = set(('browser.js', 'shell.js', 'jsref.js', 'template.js', 'user.js', 'sta.js','test262-browser.js', 'test262-shell.js','test402-browser.js', 'test402-shell.js', 'testBuiltInObject.js', 'testIntl.js','js-test-driver-begin.js', 'js-test-driver-end.js','gcstats.js','js'))

INCLUDE_NT=['ifStatement', 'iterationStatement', 'labelledStatement', 'throwStatement', 'functionDeclaration', 'arrayLiteral', 'propertyAssignment', 'propertyName', 'assignmentExpression', 'conditionalExpression', 'logicalORExpression', 'logicalANDExpression', 'bitwiseORExpression', 'bitwiseXORExpression', 'bitwiseANDExpression', 'equalityExpression', 'relationalExpression', 'shiftExpression', 'additiveExpression', 'multiplicativeExpression', 'unaryExpression', 'callExpression', 'functionExpression', 'assignmentOperator']
INCLUDE_NT=None

fileList = []

def listAllTestCasesDir(testCasesDir):
        for f in listdir(testCasesDir):
            fi=join(testCasesDir,f)
            if not isfile(fi):
                listAllTestCasesDir(fi)
            else:
                if f.endswith("js") and f not in EXCLUDE_FILES:
                    fileList.append(abspath(fi))

def createFragmentPool():
    codeFragPool=[]
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
            fileName = abspath("database" + "/" + key)
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
        
    print("Considering " + str(len(fileList)) + " files for learning code fragments")
    if not exists("database"):
        makedirs("database")
    count=1
    ind=True
    for f in fileList:
        statinfo=stat(f)
        if count > 1200 and statinfo.st_size <= 15000 :
            print (count)
            print (f)
            try:
                timeout=False
                res=extractCodeFrag(f)
                if not timeout:
                    if res is not None:
                        codeFragPool.append(res)
                
                if count % 200 == 0:
                    finalize()
                    codeFragPool=[]
            except:
                pass
        count+=1
    finalize()
    
    print ("Finished; Code generation and testing begins")

def main(fileList,args):
    try:
        status=False
        listAllTestCasesDir(testsuite)

        if args[0]=='1':
            targetDirectory=targetDirectoryName1
            shell=JS_SHELL_PATH1
            options=JS_SHELL_OPTIONS1
        elif args[0]=='2':
            targetDirectory=targetDirectoryName2
            shell=JS_SHELL_PATH2
            options=JS_SHELL_OPTIONS2
        elif args[0]=='3':
            targetDirectory=targetDirectoryName3
            shell=JS_SHELL_PATH3
            options=JS_SHELL_OPTIONS3
        else:
        	print "Invalid Arguments"
        	return

        tempDirectoryName=tmpDirectoryName+"_"+str(args[0])

        fileList2=[]
        
        if not exists(tempDirectoryName):
            makedirs(tempDirectoryName)
        if not isdir(targetDirectory):
            mkdir(targetDirectory)
        
        if len(listdir(tempDirectoryName)) == 0:
            logging.info(datetime.now())
            logging.info("Moving files that has to be processed to temporary location")
            count=0
            for file in fileList:
                statinfo = stat(file)
                if statinfo.st_size>15000:
                    continue
                from subprocess import Popen,PIPE
                exec_cmd="timeout 3 "+ shell +" -f /home/spandan/repo/geinterpreterfuzz/shell.js -f "+file
                p = Popen(exec_cmd.split(), stdout=PIPE,stderr=PIPE)
                (out,err)=p.communicate()
                rc= p.returncode
                if rc==3 and rc != 6:
                	continue
                elif rc!=0 :
                    newfname=tempDirectoryName+"/"+str(count)+"_.js"
                    temp=[]
                    errfile=config.get('Mappings','errlog')+str(args[0])
                    if isfile(errfile):
                        f2 = open(errfile, 'rb')
                        temp=load(f2)
                        f2.close()
                    if len(err)>0 and err not in temp:
                        temp.append(err)
                        f1 = open(errfile, 'wb')
                        dump(temp, f1)
                        f1.close()
                else:
                    newfname=tempDirectoryName+"/"+str(count)+".js"
                count+=1
                copyfile(file, newfname)
                fileList2.append(newfname)
            logging.info("Moved files that has to be processed to temporary location")
        else:
            logging.info("Loading file list")
            fileList[:] = []
            listAllTestCasesDir(tempDirectoryName)
            fileList2=fileList[:]
        
        from GECodeGenerator import runFuzzer         
        runFuzzer(fileList2,targetDirectory, shell,options,EXCLUDE_FILES,INCLUDE_NT,int(args[0]))
    finally:
        pass

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.setrecursionlimit(300000)
    if args[0]=="0":
        listAllTestCasesDir(testsuite)
        fileList1=listdir("database")
        if len(fileList1):
            while True:
                input1=raw_input("Do you want to Append Fragment Pool ? Y/N : ")
                if input1 in ['y','n']:
                    if input1=='y':
                        raw_input("Updating Existing Fragment Pool\n Press any key to continue...")
                        break;
                    else:
                        raw_input("Deleting Existing Fragment Pool\n Press any key to continue...")
                        for f in fileList1:
                            remove("database"+"/"+f)
                        break;

                else:
                    print "Answer must be 'Y' or 'N'"
        createFragmentPool()
    else:
        main(fileList,args)
              
