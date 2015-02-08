from py4j.java_gateway import JavaGateway  
from os import remove, getcwd, kill, chdir

from random import choice, randint
from collections import defaultdict

from threading import Thread
from subprocess import PIPE, Popen
from time import sleep, time

class AntlrParser(object):

    def __init__(self,que=None):
        self.que=que
        self.out=""
        self.p=None
        self.err=None
        self.pidList=[]
        self.input=""

    def genCodeFrag(self, parsetree, population_size,nT,subTree = None,nonTerminal=None,INCLUDE_NT_LIST =None):
        population = []
        identifers=[]
        extractIdentifiers=True
        identiferList=[]            
        for pop_count in range(0, population_size):
            #identiferList=[]            
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
                            if selectedNt in INCLUDE_NT_LIST:
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
                    if extractIdentifiers:
                        if identifier:
                            if "<<<identifier" not in v:
                                identiferList.append(v)
                                identifier=False
                        if "<<<identifier" in v:
                                identifier=True
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
                        if "<<<" not in v :
                            if ">>>" not in v:
                                subcode=subcode+" "+v
                                
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
            extractIdentifiers=False
        return population,identiferList
        
     
    def extractNonTerminal(self,val):        
        nT=[]
        for v in val:
                if "<<<" in v:
                    nT.append(v.replace("<<<","").replace(":","").strip())
        return nT
        
    def parseTree(self,input,ind=False):
        if len(input)>0:
            gateway = JavaGateway()
            parser = gateway.entry_point.getParser()
            output = parser.parseTree(input,ind) 
            gateway.close()
            return output
        return self.out
                
    def extractCodeFrag(self, fileName):
        print fileName
        parseTr=self.parseTree(fileName)
        d = defaultdict(list)
        if len(parseTr) >0:
            position = 1
            for nt in self.extractNonTerminal(parseTr.split()):
                d1 = []
                code = self.retrieveCodeFrag(parseTr, nt, position)
                if len(code) > 0:
                    if d.has_key(nt):
                        d.get(nt).append(code)
                    else:
                        d1.append(code)
                        d[str(nt)] = d1
                position += 1
        else:
            d=None
        if self.que is not None:
            self.que.put(d)
        if self.que is None:
            return d
                
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
if __name__=='__main__':
    a= AntlrParser()
    print a.parseTree("/home/spandan/geinterpreterfuzz/mozillaJSTestSuite/ecma_3/RegExp/perlstress-001.js")
