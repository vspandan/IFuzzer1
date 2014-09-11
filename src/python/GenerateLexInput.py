from os import listdir
from os.path import isfile, join
from os import system

grammar_files_path = "../../GrammarFiles"
grammar_files = [ f for f in listdir(grammar_files_path) 
                 if isfile(join(grammar_files_path, f)) ]
non_Terminals = []
terminals = []

def _msg():
    
    print "Select Grammar File"
    inc = 1
    for i in grammar_files:
        print "(" + str(inc) + ") : " + i
        inc += 1

    try:
        input = int(raw_input("Enter File Number: ")) - 1   
        if input <= len(grammar_files):
            return grammar_files_path + "/" + grammar_files[input]           
        else:
            print "\nInvalid Input"
            _msg()  
            
    except ValueError:
        print "\nInvalid Input"
        _msg()
        
def _extractNonTerminals():
    
    with open(grammar_file, 'r') as f1:
        bnf = f1.read()
        for item in bnf.split('\n'):
            if item.find(':') >= 0 :
                    key, values = item.split(':',1)
                    key = key.strip()
                    
                    non_Terminals.append(key.strip())
                    productions=values.split('|')
                    
                    for prods in productions:
                        prod=prods.split()
                        for term in prod:
                            t=term.strip()
                            if t.find("\'") >= 0  :
                                t=t[1]
                            if t not in terminals:
                                terminals.append(t)
    _extractTerminals()
    
    
                   
                    
def _extractTerminals():
    for non_Term in non_Terminals:
        if non_Term in terminals:
            terminals.remove(non_Term)        
            

    
def _createLexInput():
    with open ("../../.temp_tokens",'w') as tempfile:
        f = open("../../other/Constants", 'r');
        for line in f:
            tempfile.read(line)
            if line.strip() in terminals:
                terminals.remove(line.strip())
                f.close()
        for term in temrinals:
            tempfile.write(term)
        tempfile.close()
            
    with open("../../output/lexfile.l", 'w') as f:
       
    # definitions Begin"""
        declarations =""
        with open("../../other/ConstantDeclarations", 'r') as f1:
            declarations=f1.read()
        f.write(declarations)        
    # definitions End"""
        
    # Rules Begin"""
        
        f.write("\n%%\n")
        for term in terminals:
            if len(term) == 1:
                f.write("\""+term+ "\"\t\t{ return (\""+term+"\"); }\n")
            else :
                f.write("\""+term.lower()+ "\"\t\t{ return ("+term+"); }\n")
            
        with open("../../other/ConstantRules", 'r') as f1:
            f.write(f1.read())
        f.write("\n%%\n")
                
    # Rules End""" 
              
grammar_file = _msg()
_extractNonTerminals()
_createLexInput()

#Flex
system("flex ../../output/lexfile.l");
system("mv lex.yy.c ../../output/lex.yy.c");
#Yacc
