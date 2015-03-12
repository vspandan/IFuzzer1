from py4j.java_gateway import JavaGateway  
from os import remove, getcwd, kill, chdir

from random import choice, randint
from collections import defaultdict

from threading import Thread
from subprocess import PIPE, Popen
from time import sleep, time

import xml.etree.ElementTree as ElementTree

class AntlrParser(object):

    def __init__(self,que=None):
        self.que=que
        self.out=""
        self.nonTerminals=[]
        self.values=[]
        self.subcode =""

    def subCode(self,root):
        for child in root:
            if child.text is not None:
                self.subcode += child.text
            self.subCode(child)
            if child.tail is not None:
                self.subcode+=child.tail



    def printChild(self,root,nT,position):
        if root is not None:
            for child in root:
                self.position+=1
                if self.position==position+1 and nT == child.tag:
                    self.out += " "+nT +" "
                    if child.text is None:
                        self.subcode = ""
                    else:
                        self.subcode=child.text
                    self.subCode(child)
                    continue
                if child.tag =='identifier':
                    self.identifiers.append(child.text)
                if child.text is not None:
                    self.out+=child.text
                self.printChild(child,nT,position)   
                if child.tail is not None:
                    self.out+=child.tail
                
        

    def genCodeFrag(self, input, population_size,nT,subTree = False,nonTerminal=None,INCLUDE_NT_LIST =None):
        population = []
        identiferList=[]            
        selectedNt=None
        if len(input) > 0:
            for pop_count in range(0, population_size):
                root=None
                selectedNt=None
                self.identifiers=[]
                if len(nT) != 0: 
                    
                    if nonTerminal is None:
                        while True:
                            selected=randint(0,len(nT)-1)
                            selectedNt=nT[selected]
                            if INCLUDE_NT_LIST is not None:
                                if selectedNt in INCLUDE_NT_LIST:
                                    break
                            else:
                                 break
                    else:
                        selectedNt=nonTerminal
                        indices = [i for i, x in enumerate(nT) if x == nonTerminal]
                        selected=choice(indices)
                    try:   
                        root = ElementTree.fromstring(input)
                        if root.text is None:
                            self.out=""
                        else:
                            self.out=root.text
                    except:
                        self.out=""
                    self.position=0
                    self.printChild(root,selectedNt,selected)
                    population.append(self.out)
                    identiferList.append(self.identifiers)

        if population_size == 1: 
            if not subTree:
                return self.out,selectedNt
            if subTree: 
                return self.subcode,self.out
        return population,identiferList

    def extractNT(self,root):
        for child in root:
            self.nonTerminals.append(child.tag)
            self.extractNT(child)        
     
    def extractNonTerminal(self,input):        
        if len(input)>0:
            self.nonTerminals=[]
            try:
                root =ElementTree.fromstring(input)
                self.extractNT(root)
            except:
                pass
        return self.nonTerminals

    def extractIdent(self,root):
        for child in root:
            if child.tag == 'identifier' and child.text is not None:
                self.identifiers.append(child.text)
            self.extractIdent(child)
    
    def extractNTandText(self,root):
        for child in root:
            self.nonTerminals.append(child.tag)
            if child.text is not None:
                self.out=child.text
            else:
                self.out =""
            #self.values.append(self.getText(child))
            self.values.append(ElementTree.tostring(child,method="text"))
            self.extractNTandText(child)            

    def parseTree(self,input,ind=False):
        if len(input)>0:
            gateway = JavaGateway()
            parser = gateway.entry_point.getParser()
            output = parser.parseTree(input,ind)
            gateway.entry_point.nullify()
            gateway.close()
            parser=None
            return output
        return ""
                
    def extractCodeFrag(self, fileName):
        print fileName
        try:
            root = ElementTree.fromstring(self.parseTree(fileName))
            self.extractNTandText(root)
            d = defaultdict(list)
            for position in range(len(self.nonTerminals)):
                nt=self.nonTerminals[position]
                d1 = []
                code = self.values[position]
                if len(code) > 0:
                    if d.has_key(nt):
                        d.get(nt).append(code)
                    else:
                        d1.append(code)
                        d[str(nt)] = d1
        except :
            d=None
        if self.que is not None:
            self.que.put(d)
        if self.que is None:
            return d
    
    def extractCodeFrag_(self, fileName):
            root = ElementTree.fromstring(self.parseTree(fileName,True))
            self.extractNTandText(root)
            d = defaultdict(list)
            for position in range(len(self.nonTerminals)):
                nt=self.nonTerminals[position]
                d1 = []
                code = self.values[position]
                if len(code) > 0:
                    if d.has_key(nt):
                        d.get(nt).append(code)
                    else:
                        d1.append(code)
                        d[str(nt)] = d1
            if self.que is not None:
                self.que.put(d)
            if self.que is None:
                return d
    def init(self):
        self.aCount=0
        self.bCount=0
        self.cCount=0
        self.dCount=0
        self.a=[]
        self.b=[]
        self.c=[]
        self.d=[]

    def Analayse(self,root,aInd=False,bInd=False,cInd=False,dInd=False):
        if root is not None:
            if root.tag == 'iterationStatement':
                self.aCount+=1
                aInd=True
            elif root.tag == 'functionExpression':
            #if root.tag == 'caseClauses':
                self.bCount+=1
                aInd=True
            elif root.tag == 'ifStatement':
                self.cCount+=1
                aInd=True
            elif root.tag == 'functionDeclaration':
                self.dCount+=1
                dInd=True
            for child in root:
                self.Analayse(child,aInd,bInd,cInd,dInd)
            if root.tag == 'iterationStatement':
                self.a.append(self.aCount)
                self.aCount=0
                aInd=False
            elif root.tag == 'functionExpression':
                self.b.append(self.bCount)
                self.bCount=0
                bInd=False
            elif root.tag == 'ifStatement':
                self.c.append(self.cCount)
                self.cCount=0
                cInd=False
            elif root.tag == 'functionDeclaration':
                self.d.append(self.dCount)
                self.dCount=0
                dInd=False

    def CountNestedStructures(self,input):
        self.init()
        try:
            root = ElementTree.fromstring(self.parseTree(input,True))
            self.Analayse(root)
        except:
            pass

        return (self.a,self.b,self.c,self.d)                 
    
if __name__=='__main__':
    a= AntlrParser()
    print a.parseTree("/home/spandan/Desktop/test.js")
