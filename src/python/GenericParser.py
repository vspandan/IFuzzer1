from GenerateLexInput import *
from GenerateBisonInput import *

genLexInput =  GenerateLexInput()
genLexInput.createLexInput()
genBisonInput = GenerateBisonInput()
genBisonInput.createBisonInput(genLexInput.grammar_file)


#Flex
system("flex "+LEX_FILE);
system("bison -d -v " + BISON_FILE)
system("mv lex.yy.c ../../output/lex.yy.c");
system("mv bison.* ../../output/")
#system("cd ../../output/")
#system("ls -ltr")
#system("cc -o bison bison.tab.c lex.yy.c -ly -ll")
#system("./bison")




#Yacc
