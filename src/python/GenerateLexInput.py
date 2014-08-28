from os import listdir
from os.path import isfile, join
from os import system

grammar_files_path = "../../GrammarFiles"
grammar_files = [ f for f in listdir(grammar_files_path) 
                 if isfile(join(grammar_files_path, f)) ]
non_Terminals = []
terminals = []
keywords = []
terminal_Values=[]

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
            if item.find('::=') >= 0 :
                key, values = item.split('::=')
                key = key.strip()
                non_Terminals.append(key.strip())
            else: 
                if item.find(':') >= 0 :
                    key, values = item.split(' : ')
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
                    terminal_Values.append(values)
    
                        
def _createLexInput():
    
    with open("../../output/lexfile.l", 'w') as f:
       
    # definitions Begin"""
        declarations =""
        f.write("/***definitions***/ \n")        
        with open("../../other/ConstantDeclarations", 'r') as f1:
            declarations=f1.read()
        f.write(declarations)        
    # definitions End"""
        
    # Rules Begin"""
        f.write("\n%%\n")
        keywords=_extractKeyWords() 
        
        if keywords is not None:
            for value  in keywords:
                if value not in terminals:
                    f.write("\""+value.strip()+"\"\t\t{ return ("+value.strip()+"); }\n")
        print "Available Declarations"
        print
        print  declarations.split("%{")[0]
        print "Enter Regular Expression for following terminals"
        
        if terminals is not None:
             i=0
             for term in terminals:            
                 f.write("\""+raw_input(str(i+1)+")"+term+":"+terminal_Values[i]+"\n") + "\"\t\t{ return ("+term.strip()+"); }\n")
                 i=i+1
             
        with open("../../other/ConstantRules", 'r') as f1:
            f.write(f1.read())
        f.write("\n%%\n")        
    # Rules End"""
        
    # User Code Begins"""                
        with open("../../other/UserCode", 'r') as f1:
            f.write(f1.read())
    # User Code Ends"""
              
grammar_file = _msg()
_extractUnListedTerminals()
_createLexInput()

#Flex
system("flex ../../output/lexfile.l");
system("mv lex.yy.c ../../output/lex.yy.c");
#Yacc
