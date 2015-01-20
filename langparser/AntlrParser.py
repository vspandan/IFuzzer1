from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream
from fileinput import input
from os import remove, system, makedirs, removedirs, pathsep, path, stat

from random import choice, randint
from collections import defaultdict
from pickle import dump, load, HIGHEST_PROTOCOL

from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener
from antlr4.error.Errors import FailedPredicateException

DEFAULT_SCORE = 0
DEFAULT_DATABASE_PATH = "database"
DEFAULT_FILE = "temp"
WRITE = 'w'
APPEND = "a+"
ZERO = 0

class AntlrParser(object):

    def __init__(self,que):
        self.que=    que
    def init(self):
        self.m = defaultdict(str)
        self.non_Terminals = []
        self.rules = []
        self.count = 0;
        self.parseTr = ""
        self.pos = 0;
        self.pri = False
        self.identifiers=[]
        
    def _initParser(self, fileStream):
        self.init()
        lexer = ECMAScriptLexer(fileStream)
        stream = CommonTokenStream(lexer)
        self.parser = ECMAScriptParser(stream)
        
    def _createFileInputStream(self, program):
        fil = open(DEFAULT_FILE, WRITE);
        fil.write(program)
        fil.close()
        self.input = FileStream(DEFAULT_FILE)
        remove(DEFAULT_FILE)
    
    def parseTree(self, program=None, fileName=None, extractCF=False):
        try:
            if program is not None:
                self._createFileInputStream(program)
            else:
                if fileName is not None:
                    self.input=FileStream(fileName)
                else :
                    sys.exit()
            self._initParser(self.input)
            self.parser.buildParseTree = True
            self.rules = self.parser.ruleNames
            pContext = self.parser.program();
            if pContext.children is not None:
                self.selectSubtrees(None, pContext.getChild(0),extractCF);
            return self.parseTr
        except (AttributeError, FailedPredicateException):
            return ""
        except:
            return ""
        
    def selectSubtrees(self, nonT, s, extractCF, isIdentifier=False) :
        try:
            childCount = s.getChildCount()
            
            if childCount > 0:
                rC = s.getPayload()
                nTerminal=self.rules[rC.getRuleIndex()]
                self.parseTr = self.parseTr + "<<<" + nTerminal + ": "
                self.non_Terminals.append(nTerminal)
                if (nTerminal == 'identifier'):
                    self.identifiers.append(s.getText())
                    isIdentifier=True
                for i in range(0, childCount):
                    self.selectSubtrees(nonT, s.getChild(i),extractCF, isIdentifier)
                self.parseTr = self.parseTr + " >>> "
            else :
                if isIdentifier and extractCF:
                    self.parseTr = self.parseTr+"___identifier___"
                    isIdentifier = False
                else:
                    self.parseTr = self.parseTr+s.getText()+" "
        except:
            #TODO EOS always reaches this point. Handle this
            print 

    def extractCodeFrag(self, program=None,fileName=None):
        print fileName
        if program is not None:
            parseTr = self.parseTree(program,None,True)
        else:
            if fileName is None:
                sys.exit()
            else:
                parseTr = self.parseTree(None,fileName,True)
        d = defaultdict(dict)
        if len(parseTr) >0:
            position = 1
            directory = DEFAULT_DATABASE_PATH
            if not path.exists(directory):
                makedirs(directory)
                
            for nt in self.non_Terminals:
                code = self.retrieveCodeFrag(parseTr, self.non_Terminals, nt, position)
                if len(code) > 0:
                    d1 = defaultdict(list)
                    if d.has_key(nt):
                        """
                        if d.get(nt).has_key(code):
                            d.get(nt).get(code).append(DEFAULT_SCORE)
                        else:
                            d1[str(code)].append(DEFAULT_SCORE)
                            d.get(nt).update(d1)
                        """
                        d1[str(code)].append(DEFAULT_SCORE)
                        d.get(nt).update(d1)
                    else:
                        d1[str(code)].append(DEFAULT_SCORE)
                        d[str(nt)] = d1
                position += 1
            
            if self.que is not None:
                self.que.put(d)
            """
            nonTerms = set(self.non_Terminals)
            for nt in nonTerms:
                fileName = directory + "/" + str(nt)
                #print path.abspath(fileName)
                f = open(fileName, 'a+')
                if stat(fileName).st_size == ZERO:
                    dump(d.get(nt), f, HIGHEST_PROTOCOL)
                    f.close()
                else:
                    dictOfDict1 = load(f)
                    d1 = defaultdict(list)
                    if d.get(nt) is not None:
                        update=False
                        temp=d.get(nt)
                        keys1 = temp.keys()
                        if dictOfDict1 is not None:
                            keys = dictOfDict1.keys()
                            for key in keys1:#extracted keys
                                if key not in keys:
                                    ""
                                    temp=d.get(nt).get(key)
                                    d.get(nt).update(dictOfDict1)
                                    ""
                                    dictOfDict1[key]=temp.get(key)
                                    update=True
                                ""
                                else:
                                    d1[key] = dictOfDict1.get(key)
                                    d.get(nt).update(d1)
                                ""
                        if update:
                            f = open(fileName, 'w')
                            dump(dictOfDict1, f, HIGHEST_PROTOCOL)
            """
                
    def retrieveCodeFrag(self, pTreeRepr, nT, nonT, position):
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

if __name__ == '__main__':
        p = AntlrParser()
        #p.extractCodeFrag("function sp(e)\r\n" + "{\r\n" + "var x = null;\r\n" + "var y = true + 3;\r\n" + "}\r\n")
        #p.extractCodeFrag("var a=function (x,y){x=10000+this.y;};")
        #p.extractCodeFrag("var a=10000+\"s\"+6.4;")
        input=raw_input()
        print input
        #p.extractCodeFrag(None,input)
        print p.parseTree(None,input)
