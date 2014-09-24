
OUTPUT_PATH = "output"
DIR="~/Documents/GePyNeurgen/"
TEMP_FILE1="/temp1"
TEMP_FILE2="/temp2"
LEX_FILE="/lexfile.l"
BISON_FILE="/bison.y"
NEW_LINE='\n'
RULE_DELIM = ':'
PROD_DELIMITER1='|'
RULE_END_DELIM=';'
FILE_SEPERATOR="/"
SINGLE_QUOTE="\'"

REG_EX="DIGIT\t\t\t[0-9]"+ NEW_LINE +"HEX_DIGIT\t\t\t[0-9a-fA-F]"+ NEW_LINE +"HEX_INTEGER\t\t\t0[Xx]{HEX_DIGIT}+"+ NEW_LINE +"INTEGER\t\t\t{DIGIT}+"+NEW_LINE+"EXPONENT\t\t\t[Ee][-+]?{INTEGER}"+NEW_LINE+"DOUBLE\t\t\t{INTEGER}\".\"{DIGIT}*{EXPONENT}?"+NEW_LINE+"STRING\t\t\t \\\"[^\"\\n]*\\\""+NEW_LINE+"IDENTIFIER\t\t\t[a-zA-Z][a-zA-Z_0-9]*"+NEW_LINE+"ARITH_OP\t\t\t([+/*%])"+NEW_LINE+"REL_OP\t\t\t[<|>]" 
RULES="{STRING}\t\t\t\t{ yylval.c=strdup(yytext); return STRING_LITERAL; }"+NEW_LINE+"{INTEGER}\t\t\t\t{ yylval.c=strdup(yytext); return INT_LITERAL; }"+NEW_LINE+"{DOUBLE}\t\t\t\t{ yylval.c=strdup(yytext); return INT_LITERAL; }"+NEW_LINE+"{HEX_INTEGER}\t\t\t\t{ yylval.c=strdup(yytext);  return INT_LITERAL; }"+NEW_LINE+"{IDENTIFIER}\t\t\t\t{ yylval.c=strdup(yytext); return ID;  }"
IMPORTS=NEW_LINE +"%{" + NEW_LINE + "#include \"bison.tab.h\"" +NEW_LINE + "#include <stdio.h>"+ NEW_LINE + "#include <stdlib.h>"  + NEW_LINE +"%}"
READ  = 'r'
WRITE = 'w'

CONSTANTS="ASSIGN_OP INT_LITERAL STRING_LITERAL ID E_ASSIGN_OP CHAR_LITERAL EQ_OP COND_OP REL_OP ARITH_OP"