from GenerateLexInput import *
from GenerateBisonInput import *

genLexInput =  GenerateLexInput()
genLexInput.createLexInput()
genBisonInput = GenerateBisonInput()
genBisonInput.createBisonInput(genLexInput.grammar_file)


#Flex
system("flex -w "+LEX_FILE);
system("bison -d -v " + BISON_FILE)
system("mv lex.yy.c ../../output/lex.yy.c");
system("mv bison.* ../../output/")
