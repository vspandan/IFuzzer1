from Property import * 
from os import listdir
from os.path import isfile, join
from os import system


class GenerateLexInput(object):

    def __init__(self):
        
        self.grammar_files = [ f for f in listdir(GRAMMAR_FILES_FOLDER) 
                 if isfile(join(GRAMMAR_FILES_FOLDER, f)) ]
        self.non_Terminals = []
        self.terminals = []
        self.grammar_file =None

    def _msg(self):
        
        print "Select Grammar File"
        inc = 1
        for i in self.grammar_files:
            print "(" + str(inc) + ") : " + i
            inc += 1
    
        try:
            input = int(raw_input("Enter File Number: ")) - 1   
            if input <= len(self.grammar_files):
                self.grammar_file = GRAMMAR_FILES_FOLDER + FILE_SEPERATOR + self.grammar_files[input]                           
            else:
                print "\nInvalid Input"
                self._msg()  
                
        except ValueError:
            print "\nInvalid Input"
            self._msg()
            
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
        with open (TEMP_FILE1,WRITE) as tempfile1:
            tokens =self.terminals
            f = open(CONSTANTS, READ);
            for line in f:
                if (line.strip() not in tokens) :
                    tokens.append(line.strip())
            with open (TEMP_FILE2,WRITE) as tempfile2:
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
        
        self._msg()
        self._extractNonTerminals()
        self._extractTerminals()
        self._generateTokens()
        with open(LEX_FILE, WRITE) as f:
    
        # definitions Begin"""
            declarations =""
            with open(DECLARATIONS, READ) as f1:
                declarations=f1.read()
            f.write(declarations)        
            # definitions End"""
            f.write(NEW_LINE)
            f.write(NEW_LINE +"%{" + NEW_LINE + "#include \"bison.tab.h\"" +NEW_LINE + "#include <stdio.h>"+ NEW_LINE + "#include <stdlib.h>"  + NEW_LINE +"%}")
            f.write(NEW_LINE)
            # Rules Begin"""
            
            f.write(NEW_LINE+"%%"+NEW_LINE)
            for term in self.terminals:
                if term.find(SINGLE_QUOTE) >= 0 :
                    if len(term) == 3:
                        term=term.replace("\'","")
                        f.write("\""+term+ "\"\t\t{ yylval.c=strdup(yytext); return yytext[0]; }\n")
                    else:
                        term=term.replace("\'","\"")
                        f.write(term+ "\t\t{ yylval.c=strdup("+term+"); return " +term+" }\n")
                else :
                    f.write("\""+term.lower()+ "\"\t\t{ yylval.c=strdup(yytext); return ("+term+"); }\n")
                
            with open(RULES_FILE, ) as f1:
                f.write(f1.read())
            
            f.write(NEW_LINE+"%%"+NEW_LINE)                    
        # Rules End""" 
                  
