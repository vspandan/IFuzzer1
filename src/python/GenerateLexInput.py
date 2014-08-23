from os import listdir
from os.path import isfile, join
from os import system

grammar_files_path = "../../GrammarFiles"
grammar_files = [ f for f in listdir(grammar_files_path) if isfile(join(grammar_files_path, f)) ]
non_Terminals = []
terminals = []
keywords = []
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
        
def _extractKeyWords():
    
    with open(grammar_file, 'r') as f1:
        bnf = f1.read()
        for item in bnf.split('\n'):
            if item.find('::=') >= 0:
                key, values = item.split('::=')
                key = key.strip()
                if key == "KEYWORD" :
                    return values.split('|')
                
def _extractNonTerminals():
    
    with open(grammar_file, 'r') as f1:
        bnf = f1.read()
        for item in bnf.split('\n'):
            if item.find('::=') >= 0:
                key, values = item.split('::=')
                key = key.strip()
                non_Terminals.append(key.strip())

def _extractUnListedTerminals():
    
    _extractNonTerminals()    
    with open(grammar_file, 'r') as f1:
        bnf = f1.read()
        for item in bnf.split('\n'):
            if item.find('::=') >= 0:
                key, values = item.split('::=')
                valu= values.split('|')
                isTerm=True
                for val in valu:
                    if val in non_Terminals:
                        isTerm=False
                if isTerm:
                    terminals.append(key)
    print terminals
    
                        
def _createLexInput():
    
    with open("../../output/lexfile.l", 'w') as f:
        # definitions Begin"""
        f.write("/***definitions***/ \n")        
        with open("../../other/ConstantDeclarations", 'r') as f1:
            f.write(f1.read())
        # definitions End"""
        
        # Rules Begin"""
        f.write("\n%%\n")
        keywords=_extractKeyWords() 
        for value  in keywords:
            f.write("\""+value.strip()+"\"\t\t{ return ("+value.strip()+"); }\n")
            
        for term in terminals:            
            f.write("\""+raw_input("Enter Regular Expression for "+ term) + "\"\t\t{ return ("+term.strip()+"); }\n")
        ## Constant Rules 
        with open("../../other/ConstantRules", 'r') as f1:
            f.write(f1.read())
        f.write("\n%%\n")
        # Rules End"""
        
        # User Code Begins"""                
        with open("../../other/UserCode", 'r') as f1:
            f.write(f1.read())
        # User Code Ends"""
              
grammar_file = _msg()
print grammar_file
_extractUnListedTerminals()
_createLexInput()
#Flex
system("flex ../../output/lexfile.l");
system("mv lex.yy.c ../../output/lex.yy.c");
#Yacc
