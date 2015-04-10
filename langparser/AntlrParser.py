from os import path

from random import choice, randint
from collections import defaultdict

from re import split
import sys
sys.path.append(path.dirname(path.abspath(__file__))+"/ECMAScript.jar")
sys.path.append(path.dirname(path.abspath(__file__))+"/antlr-4.5-rc-2-complete.jar")
from langparser import CodeFragmentExtractor
import xml.etree.ElementTree as ElementTree


globalobj=['Infinity', 'NaN', 'undefined', 'null ', 'eval', 'uneval', 'isFinite', 'isNaN', 'parseFloat', 'parseInt', 'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'escape', 'unescape', 'Object', 'Function', 'Boolean', 'Symbol', 'Error', 'EvalError', 'InternalError', 'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'Number', 'Math', 'Date', 'String', 'RegExp', 'Array', 'Int8Array', 'Uint8Array', 'Uint8ClampedArray', 'Int16Array', 'Uint16Array', 'Int32Array', 'Uint32Array', 'Float32Array', 'Float64Array', 'Map', 'Set', 'WeakMap', 'WeakSet', 'Promise', 'Generator', 'GeneratorFunction', 'ArrayBuffer', 'DataView', 'JSON', 'Reflect', 'Proxy', 'Iterator', 'ParallelArray', 'StopIteration']

class AntlrParser(object):

    def __init__(self,que=None):
    	self.que=que
        self.out=""
        self.nonTerminals=[]
        self.values=[]
        self.subcode ={}
        
    def subCodeGen(self,root,pos):
        # self.parser = self.gateway.entry_point.getCodeFragmentExtractor()
		for child in root:
			self.position+=1
			if child.text is not None:
				if child.tag == 'identifier' and child.text not in globalobj:
					self.subcode[pos] = self.subcode[pos]+" _id_"+child.text
				else:
					self.subcode[pos] = self.subcode[pos]+child.text
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
                            self.subcode[self.position-1]=child.text
                        self.subCodeGen(child,self.position-1)
                        continue
                if child.text is not None:
                    self.out+=child.text
                self.printChild(child,nTList)   
                if child.tail is not None:
                    self.out+=child.tail

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

    def extractNTandText(self,root):
        if root is not None:
            for child in root:
            	print child.tag
            	self.nonTerminals.append(child.tag)
                txt=ElementTree.tostring(child,method="text")
                self.values.append(txt)
                if len(list(child)) >1:
            		print child.tag
	                print txt
                self.extractNTandText(child)       

    def genCodeFrag(self, input,nT,subTree = False,nonTerminal=None,INCLUDE_NT_LIST = None, count=1):
        selectedNTList={}
        self.subcode={}
        self.out=""
        
        try: 
            if len(input) > 0 and len(nT) != 0:
                root=None
                internalCount=0
                while internalCount < count :
                    selectedNt=None
                    if nonTerminal is None:
                        while True:
                            selected=randint(0,len(nT)-1)
                            selectedNt=nT[selected]
                            if INCLUDE_NT_LIST is None:
                                break;
                            if selectedNt in INCLUDE_NT_LIST : 
                                break
                    else:
                        selectedNt=nonTerminal[internalCount]
                        indices = [i for i, x in enumerate(nT) if x == nonTerminal[internalCount]]
                        selected=choice(indices)

                    internalCount+=1
                    selectedNTList[selected]=selectedNt
                    root = ElementTree.fromstring(input)
                    if root.text is not None:
                        self.out=root.text
                self.position=0
                self.printChild(root,selectedNTList)
        except:
            pass
        if not subTree:
            return self.out,selectedNTList
        if subTree: 
            return self.subcode,self.out,selectedNTList

    def parseTree(self,input,ind=False):
        if len(input)>0:
            c=CodeFragmentExtractor()
            output = c.XMLIRGenerator(input,ind)
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
    def extractCodeFrag(self, fileName):
        print fileName
        # output,identifiers=self.parseTree(fileName,False)
        
        # root = ElementTree.fromstring(output)
        # self.extractNTandText(root)
        # d = defaultdict(list)
        # for position in range(len(self.nonTerminals)):
        #         nt=self.nonTerminals[position]
        #         d1 = []
        #         code = self.values[position]
        #         if len(code) > 0:
        #             if d.has_key(nt):
        #                 d.get(nt).append(code)
        #             else:
        #                 d1.append(code)
        #                 d[str(nt)] = d1
        c=CodeFragmentExtractor()
        d=c.extractFrags(fileName,True)
        if self.que is not None:
            self.que.put(d)
        if self.que is None:
            return d

    
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

    def CountNestedStructures(self,output):
    	self.aCount=0
    	self.bCount=0
    	self.cCount=0
    	self.dCount=0
    	self.a=[]
    	self.b=[]
    	self.c=[]
    	self.d=[]
    	try:
    		root = ElementTree.fromstring(output)
    		self.Analayse(root)
    	except:
    		pass
    	return (self.a,self.b,self.c,self.d)                 

if __name__ == '__main__':
    a= AntlrParser()
    print a.parseTree("/home/spandan/test.js",False)
    print a.extractCodeFrag("/home/spandan/test.js")