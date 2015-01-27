from fileinput import input
from os import remove, system, makedirs, removedirs, pathsep, path, stat,getcwd

from random import choice, randint
from collections import defaultdict
from pickle import dump, load, HIGHEST_PROTOCOL


import subprocess

DEFAULT_SCORE = 0
DEFAULT_DATABASE_PATH = "database"
DEFAULT_FILE = "temp"
WRITE = 'w'
APPEND = "a+"
ZERO = 0

class AntlrParser(object):

    def __init__(self,dBDir=None):
        DEFAULT_DATABASE_PATH=dBDir


    def genCodeFrag(self, parsetree, population_size,nT,subTree = None,nonTerminal=None,INCLUDE_NT_LIST =None):
        population = []
        identifers=[]
        for pop_count in range(0, population_size):
            identiferList=[]            
            identifier=False
            val=parsetree.split()
            code=""
            subcode=""
            selectedNt=None
            if len(nT) != 0: 
                
                if nonTerminal is None:
                    while True:
                        self.selected=randint(0,len(nT)-1)
                        selectedNt=nT[self.selected-1]
                        if INCLUDE_NT_LIST is not None:
                            if selectedNT in INCLUDE_NT_LIST:
                                break
                        else:
                            break
                else:
                    selectedNt=nonTerminal
                    indices = [i for i, x in enumerate(nT) if x == nonTerminal]
                    self.selected=choice(indices)+1
                    
                nTposition=0;
                indicator = False
                temp=0
                
                for v in val:
                    
                    if '<<<' in v:
                        nTposition=nTposition+1
                        if indicator:
                            temp=temp+1
                        
                    if nTposition == self.selected and not indicator:
                        nTposition =-10000
                        code=code+" "+selectedNt
                        indicator=True                    
                        temp=temp+1
                        
                    if '>>>' in v:
                        if indicator:
                            temp=temp-1
                            
                    if indicator:
                        #for complete parse representation that is being replaced use below code statement.
                        #subcode=subcode + " " +v
                        if "<<<identifier" in v:
                            identifier=True
                        if "<<<" not in v :
                            if ">>>" not in v:
                                subcode=subcode+" "+v
                                if identifier:
                                    identiferList.append(v)
                                    identifier=False
                    if not indicator:
                        if "<<<" not in v :
                            if ">>>" not in v:
                                code=code+" "+v
                    
                    if temp==0 and indicator:
                        indicator=False
                    
            if population_size == 1: 
                if subTree is None:
                    return code.strip(),selectedNt
                if subTree is not None:                    
                    return subcode.strip()
            identifers.append(identiferList)
            population.append(code.strip())
        

        return population,identifers
        
     
    def extractNonTerminal(self,val):        
        nT=[]
        for v in val:
                if "<<<" in v:
                    nT.append(v.replace("<<<","").replace(":","").strip())
        return nT

    def parseTree_(self,program):
        p = subprocess.Popen(["sh parser.sh null "+program ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        return out


    def parseTree(self,fileName):
        p = subprocess.Popen(["sh parser.sh "+fileName ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        print out
        return out
        

    def extractCodeFrag(self, fileName):
        parseTr=self.parseTree(fileName)
        print fileName
        d = defaultdict(dict)
        if len(parseTr) >0:
            position = 1
            directory = DEFAULT_DATABASE_PATH
            if not path.exists(directory):
                makedirs(directory)
                
            for nt in self.extractNonTerminal(parseTr.split()):
                code = self.retrieveCodeFrag(parseTr, nt, position)
                if len(code) > 0:
                    d1 = defaultdict(list)
                    if d.has_key(nt):
                        d.get(nt).update(d1)
                    else:
                        d1[str(code)].append(DEFAULT_SCORE)
                        d[str(nt)] = d1
                position += 1
            for key in d.keys():
                    fileName = directory + "/" + key
                    f = open(fileName, 'a+')
                    if stat(fileName).st_size == 0:
                        dump(d.get(key), f, HIGHEST_PROTOCOL)
                    else:
                        temp=load(f)
                        temp.update(d.get(key))
                        f.close()
                        f = open(fileName, 'w')
                        dump(temp, f, HIGHEST_PROTOCOL)
                    f.close()
            
                
    def retrieveCodeFrag(self, pTreeRepr, nonT, position):
            val = pTreeRepr.split()
            posTrack = 0;
            indicator = False
            temp = 0
            subcode = ""
            
            for v in val:
                
                if '<<<' in v:
                    posTrack = posTrack + 1
                    if indicator:
                        temp = temp + 1
                    
                if posTrack == position and not indicator:
                    posTrack = -10000
                    indicator = True                    
                    temp = temp + 1
                    
                if '>>>' in v:
                    if indicator:
                        temp = temp - 1
                        
                if indicator:
                    if "<<<" not in v :
                        if ">>>" not in v:
                            subcode = subcode + " " + v
                
                if temp == 0 and indicator:
                    indicator = False
            return subcode.strip()
