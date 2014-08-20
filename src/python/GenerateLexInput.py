from os import listdir
from os.path import isfile, join

grammar_files_path = "../../GrammarFiles"
grammar_files = [ f for f in listdir(grammar_files_path) if isfile(join(grammar_files_path, f)) ]

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

def _createLexInput():

    with open("../../output/lexfile.l", 'w') as f:
        
        #definitions Begin
        f.write("/***definitions***/ \n")
        f.write("digit   [0-9] \n" )
        f.write("delimiter   [\t\n :;] \n" )
        f.write("ws   {delimiter}+ \n" )
        f.write("letter   [A-Za-z] \n")
        f.write("id   {letter}({letter}|{digit})* \n")
        f.write("number   {digit}+(\.{digit}+)?(E[+-]?{digit}+)? \n")
        #definitions End
        
        #Rules Begin
        f.write("\n%%\n")
        f.write("/***rules***/ \n")
        f.write(".   {ECHO; yyerror(\"unexpected character\");}")
        
        #Rules End
        
        #User Code Begins
        f.write("\n%%\n")
        f.write("/***user code***/ \n")
        #User Code Ends
                
grammar_file = _msg()
# print grammar_file

_createLexInput()
        
        
        
        
