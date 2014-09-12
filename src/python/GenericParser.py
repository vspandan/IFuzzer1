from GenerateLexInput import *
from GenerateBisonInput import *

genLexInput =  GenerateLexInput()
genLexInput.createLexInput()
genBisonInput = GenerateBisonInput()
genBisonInput.createBisonInput(genLexInput.grammar_file)


#Flex
system("flex ../../output/lexfile.l");
system("mv lex.yy.c ../../output/lex.yy.c");
#Yacc
