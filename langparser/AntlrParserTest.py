from os import path
from copy import deepcopy
from random import choice
from collections import defaultdict

from re import split
import sys
sys.path.append(path.dirname(path.abspath(__file__))+"/ECMAScript.jar")
sys.path.append(path.dirname(path.abspath(__file__))+"/antlr-4.5-rc-2-complete.jar")
from langparser import CodeFragmentExtractor
import xml.etree.ElementTree as ElementTree
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')


LOG_FILENAME="s"
import logging

logging.basicConfig(filename=LOG_FILENAME,
                    level=10,
                    )

globalobj=['Infinity', 'NaN', 'undefined', 'null ', 'eval', 'uneval', 'isFinite', 'isNaN', 'parseFloat', 'parseInt', 'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'escape', 'unescape', 'Object', 'Function', 'Boolean', 'Symbol', 'Error', 'EvalError', 'InternalError', 'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'Number', 'Math', 'Date', 'String', 'RegExp', 'Array', 'Int8Array', 'Uint8Array', 'Uint8ClampedArray', 'Int16Array', 'Uint16Array', 'Int32Array', 'Uint32Array', 'Float32Array', 'Float64Array', 'Map', 'Set', 'WeakMap', 'WeakSet', 'Promise', 'Generator', 'GeneratorFunction', 'ArrayBuffer', 'DataView', 'JSON', 'Reflect', 'Proxy', 'Iterator', 'ParallelArray', 'StopIteration']

def extractNonTerminal(input,nonTerminals):        
    def extractNT(root,nonTerminals):
        for child in root:
            nonTerminals.append(child.tag)
            extractNT(child,nonTerminals)    
        return nonTerminals
    if len(input)>0:
        try:
            root =ElementTree.fromstring(input)
            nonTerminals=extractNT(root,nonTerminals)
        except:
            pass
    return nonTerminals

# def extractNTandText(root):
#     if root is not None:
#         for child in root:
#             nonTerminals.append(child.tag)
#             txt=ElementTree.tostring(child,method="text")
#             values.append(txt)
#             extractNTandText(child)       

def genCodeFrag(input,nT,nonTerminal=None,INCLUDE_NT_LIST = None, count=1):
    class Temp(object):
        def __init__(self):
            self.position=0
            self.out=""
            self.subcode={}

        def subCodeGen(self,root,pos):
            for child in root:
                self.position+=1
                if child.text is not None:
                    if child.tag == 'identifier' and child.text not in globalobj:
                        self.subcode[pos]=self.subcode[pos]+" _id_"+child.text
                    else:
                        self.subcode[pos]=self.subcode[pos]+child.text
                self.subCodeGen(child,pos)
                if child.tail is not None:
                    self.subcode[pos]=self.subcode[pos]+child.tail
            
        def printChild(self,root,nTList):
            if root is not None:
                for child in root:
                    self.position+=1
                    if nTList.has_key(self.position-1):
                        if nTList[self.position-1]==child.tag:
                            self.out += " "+child.tag +" "
                            if child.text is None:
                                self.subcode[self.position-1] = ""
                            else:
                                self.subcode[self.position-1] = child.text
                            self.subCodeGen(child,self.position-1)
                            if child.tail is not None:
                                self.out+=child.tail
                            continue
                    if child.text is not None:
                        self.out+=child.text
                    self.printChild(child,nTList)   
                    if child.tail is not None:
                        self.out+=child.tail
            return self.subcode,self.out
    logging.info("GenCodeFrag method - Entered ")
    selectedNTList={}
    subcode={}
    out=""
    try: 
        
        if len(input) > 0 and len(nT) > 0:
            proceed=True
            root=None
            internalCount=0
            while internalCount < count :
                selectedNt=None
                if nonTerminal is None:
                    tempNT=deepcopy(nT)
                    while True:
                        selectedNt=choice(tempNT)
                        if INCLUDE_NT_LIST is None:
                            break;
                        tempNT.remove(selectedNt)
                        if selectedNt in INCLUDE_NT_LIST : 
                            proceed=True
                            break
                        if len(tempNT) <= 0:
                            proceed=False
                            break
                        
                else:
                    selectedNt=nonTerminal[internalCount]
                indices = [i for i, x in enumerate(nT) if x == selectedNt]
                selected=choice(indices)
                internalCount+=1
                selectedNTList[selected]=selectedNt
                root = ElementTree.fromstring(input)
                t=Temp()
                if root.text is not None:
                    t.out=root.text
            if proceed:
                subcode,out=t.printChild(root,selectedNTList)
    except:
        pass
    finally:
        logging.info("GenCodeFrag method - Completed ")
        return subcode,out,selectedNTList

def parseTree(input,ind=False):
    if len(input)>0:
        c=CodeFragmentExtractor()
        output = c.XMLIRGenerator(input,ind)
        c=None
        identifiers_JavaObj=output['identifiers']
        identifiers=[]
        for id in identifiers_JavaObj:
            identifiers.append(id)
        # xmlCode=''.join(split('(\W+)',output['parsecode']))
        return output['parsecode'],identifiers
        # return xmlCode,identifiers
    return "",[]
"""
Restricting to accept only files;
"""
def extractCodeFrag(fileName,que=None):
    logging.info(fileName)
    # output,identifiers=parseTree(fileName,False)
    
    # root = ElementTree.fromstring(output)
    # extractNTandText(root)
    # d = defaultdict(list)
    # for position in range(len(nonTerminals)):
    #         nt=nonTerminals[position]
    #         d1 = []
    #         code = values[position]
    #         if len(code) > 0:
    #             if d.has_key(nt):
    #                 d.get(nt).append(code)
    #             else:
    #                 d1.append(code)
    #                 d[str(nt)] = d1
    c=CodeFragmentExtractor()
    d=c.extractFrags(fileName,True)
    c=None
    if que is not None:
        que.put(d)
    if que is None:
        return d




def CountNestedStructures(output):
    a=[]
    b=[]
    c=[]
    d=[]

    def Analayse(root,aCount=0,bCount=0,cCount=0,dCount=0,aInd=False,bInd=False,cInd=False,dInd=False):

        if root is not None:
            if root.tag == 'iterationStatement':
                aCount+=1
                aInd=True
            elif root.tag == 'functionExpression':
            #if root.tag == 'caseClauses':
                bCount+=1
                aInd=True
            elif root.tag == 'ifStatement':
                cCount+=1
                aInd=True
            elif root.tag == 'functionDeclaration':
                dCount+=1
                dInd=True
            for child in root:
                Analayse(child,aCount,bCount,cCount,dCount,aInd,bInd,cInd,dInd)
            if root.tag == 'iterationStatement':
                a.append(aCount)
                aCount=0
                aInd=False
            elif root.tag == 'functionExpression':
                b.append(bCount)
                bCount=0
                bInd=False
            elif root.tag == 'ifStatement':
                c.append(cCount)
                cCount=0
                cInd=False
            elif root.tag == 'functionDeclaration':
                d.append(dCount)
                dCount=0
                dInd=False

    try:
        root = ElementTree.fromstring(output)
        Analayse(root)
    except:
        pass
    return (a,b,c,d)                 

if __name__ == '__main__':
    print parseTree("/home/spandan/test.js",False)
    print extractCodeFrag("/home/spandan/test.js")
    