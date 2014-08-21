/***definitions***/ 
DIGIT		([0-9])
IDENTIFIER 	([a-zA-Z][a-zA-Z_0-9]*)
NUMBER		({DIGIT}+(\.{DIGIT}+)?(E[+-]?{DIGIT}+)?)
STRING		{[A-Za-z_]}?\"(\\.|[^\\"])*\"
HEX		([a-fA-F0-9])
HEXINTEGER	(0[xX]{HEX}+)
DELIMITER	([ \t\v\n\f])

%{
#include <stdio.h>
#include "y.tab.h"
%}
 

%%
"auto"			{ return(T_AUTO); }
"extern"		{ return(T_EXTERN); }
"..."			{ return(T_ELLIPSIS); }
">>="			{ return(T_RIGHT_ASSIGN); }
"<<="			{ return(T_LEFT_ASSIGN); }
"+="			{ return(T_ADD_ASSIGN); }
"-="			{ return(T_SUB_ASSIGN); }
"*="			{ return(T_MUL_ASSIGN); }
"/="			{ return(T_DIV_ASSIGN); }
"%="			{ return(T_MOD_ASSIGN); }
"&="			{ return(T_AND_ASSIGN); }
"^="			{ return(T_XOR_ASSIGN); }
"|="			{ return(T_OR_ASSIGN); }
">>"			{ return(T_RIGHT_OP); }
"<<"			{ return(T_LEFT_OP); }
"++"			{ return(T_INC_OP); }
"--"			{ return(T_DEC_OP); }
"->"			{ return(T_PTR_OP); }
"&&"			{ return(T_AND_OP); }
"||"			{ return(T_OR_OP); }
"<="			{ return(T_LE_OP); }
">="			{ return(T_GE_OP); }
"=="			{ return(T_EQ_OP); }
"!="			{ return(T_NE_OP); }
";"			{ return(';'); }
("{"|"<%")		{ return('{'); }
("}"|"%>")		{ return('}'); }
","			{ return(','); }
":"			{ return(':'); }
"="			{ return('='); }
"("			{ return('('); }
")"			{ return(')'); }
("["|"<:")		{ return('['); }
("]"|":>")		{ return(']'); }
"."			{ return('.'); }
"&"			{ return('&'); }
"!"			{ return('!'); }
"~"			{ return('~'); }
"-"			{ return('-'); }
"+"			{ return('+'); }
"*"			{ return('*'); }
"/"			{ return('/'); }
"%"			{ return('%'); }
"<"			{ return('<'); }
">"			{ return('>'); }
"^"			{ return('^'); }
"|"			{ return('|'); }
"?"			{ return('?'); }

%%
yywrap()
{
	return(1);
}
