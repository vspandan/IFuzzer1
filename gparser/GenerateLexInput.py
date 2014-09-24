from Property import * 
from os import listdir
from os.path import isfile, join
from os import system
from os import stat
from os import mkdir
from os import path

class GenerateLexInput(object):
    
    
    def getSelectedGrammar (self,fileName):
        self.grammar_file =fileName

    
    def setSelectedGrammar (self,fileName):
        self.grammar_file =fileName

    def __init__(self):
        
        self.non_Terminals = []
        self.terminals = []
        self.grammar_file =None
        self.HOME_DIR=path.expanduser(DIR)
        try:
            stat(self.HOME_DIR)
        except:
            mkdir(self.HOME_DIR)  

    def _extractNonTerminals(self):
        st=[]
        with open(self.grammar_file, READ) as f1:
            bnf = f1.read()
            for item in bnf.split(NEW_LINE):
                if item.find(RULE_DELIM) >= 0 :
                        key, values = item.split(RULE_DELIM,1)
                        key = key.strip()
                        
                        self.non_Terminals.append(key.strip())
                        productions=values.split(PROD_DELIMITER1)
                        
                        for prods in productions:
                            prod=prods.split()
                            for term in prod:
                                t=term.strip()
                                if t not in self.terminals:
                                    self.terminals.append(t)
                                    
    def _extractTerminals(self):
        for non_Term in self.non_Terminals:
            if non_Term in self.terminals:
                self.terminals.remove(non_Term)        
                
    
    def _generateTokens(self):
        with open (self.HOME_DIR+TEMP_FILE1,WRITE) as tempfile1:
            tokens =self.terminals
            for const in CONSTANTS.split():
                if (const not in tokens) :
                    tokens.append(const)
            with open (self.HOME_DIR+TEMP_FILE2,WRITE) as tempfile2:
                for t in tokens:
                    if t.find(SINGLE_QUOTE)  == -1 :
                        if len(t) !=1 :
                            tempfile1.write(t + " ")
                    else :
                        if len(t) > 3:
                            tempfile2.write(t + " ")
                        
            tempfile1.close()
            tempfile2.close()
    
        
    def createLexInput(self):
            
        self._extractNonTerminals()
        self._extractTerminals()
        self._generateTokens()
        
        
        
        with open(self.HOME_DIR+LEX_FILE, WRITE) as f:

            f.write(REG_EX)        
            f.write(NEW_LINE)
            f.write(IMPORTS)
            f.write(NEW_LINE)
            f.write(NEW_LINE+"%%"+NEW_LINE)
            for term in self.terminals:
                if term.find(SINGLE_QUOTE) >= 0 :
                    if len(term) == 3:
                        term=term.replace("\'","")
                        f.write("\""+term+ "\"\t\t{ yylval.c=strdup(yytext); return yytext[0]; }\n")
                    else:
                        term=term.replace("\'","\"")
                        f.write(term+ "\t\t{ yylval.c=strdup("+term+"); return " +term+"; }\n")
                else :
                    f.write("\""+term.lower()+ "\"\t\t{ yylval.c=strdup(yytext); return ("+term+"); }\n")
            
            f.write(RULES)
            f.write(NEW_LINE+"%%"+NEW_LINE)                    
                  

