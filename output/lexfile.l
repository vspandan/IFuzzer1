DIGIT		       	[0-9]
HEX_DIGIT  	      	[0-9a-fA-F]
HEX_INTEGER       	0[Xx]{HEX_DIGIT}+
INTEGER           	{DIGIT}+
EXPONENT          	[Ee][-+]?{INTEGER}
DOUBLE          	{INTEGER}"."{DIGIT}*{EXPONENT}?
STRING  	  	\"[^"\n]*\"
IDENTIFIER        	[a-zA-Z][a-zA-Z_0-9]*
ARITH_OP		([+/*%])
REL_OP			[<|>]

%{
#include "bison.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

%%
"class"		{ yylval.c=strdup(yytext); return (CLASS); }
"program"		{ yylval.c=strdup(yytext); return (Program); }
"{"		{ yylval.c=strdup(yytext); return yytext[0]; }
"}"		{ yylval.c=strdup(yytext); return yytext[0]; }
";"		{ yylval.c=strdup(yytext); return yytext[0]; }
","		{ yylval.c=strdup(yytext); return yytext[0]; }
"id"		{ yylval.c=strdup(yytext); return (ID); }
"["		{ yylval.c=strdup(yytext); return yytext[0]; }
"int_literal"		{ yylval.c=strdup(yytext); return (INT_LITERAL); }
"]"		{ yylval.c=strdup(yytext); return yytext[0]; }
"("		{ yylval.c=strdup(yytext); return yytext[0]; }
")"		{ yylval.c=strdup(yytext); return yytext[0]; }
"void"		{ yylval.c=strdup(yytext); return (VOID); }
"int"		{ yylval.c=strdup(yytext); return (INT); }
"boolean"		{ yylval.c=strdup(yytext); return (BOOLEAN); }
"if"		{ yylval.c=strdup(yytext); return (IF); }
"else"		{ yylval.c=strdup(yytext); return (ELSE); }
"for"		{ yylval.c=strdup(yytext); return (FOR); }
"e_assign_op"		{ yylval.c=strdup(yytext); return (E_ASSIGN_OP); }
"return"		{ yylval.c=strdup(yytext); return (RETURN); }
"break"		{ yylval.c=strdup(yytext); return (BREAK); }
"continue"		{ yylval.c=strdup(yytext); return (CONTINUE); }
"assign_op"		{ yylval.c=strdup(yytext); return (ASSIGN_OP); }
"callout"		{ yylval.c=strdup(yytext); return (CALLOUT); }
"string_literal"		{ yylval.c=strdup(yytext); return (STRING_LITERAL); }
"arith_op"		{ yylval.c=strdup(yytext); return (ARITH_OP); }
"minus"		{ yylval.c=strdup(yytext); return (MINUS); }
"rel_op"		{ yylval.c=strdup(yytext); return (REL_OP); }
"eq_op"		{ yylval.c=strdup(yytext); return (EQ_OP); }
"cond_op"		{ yylval.c=strdup(yytext); return (COND_OP); }
"!"		{ yylval.c=strdup(yytext); return yytext[0]; }
"true"		{ yylval.c=strdup(yytext); return (TRUE); }
"false"		{ yylval.c=strdup(yytext); return (FALSE); }
"char_literal"		{ yylval.c=strdup(yytext); return (CHAR_LITERAL); }
{STRING} 		{ yylval.c=strdup(yytext); return STRING_LITERAL; }
{INTEGER}		{ yylval.c=strdup(yytext); return INT_LITERAL; }
{DOUBLE}		{ yylval.c=strdup(yytext); return INT_LITERAL; }
{HEX_INTEGER}     	{ yylval.c=strdup(yytext);  return INT_LITERAL; }
{IDENTIFIER}            { yylval.c=strdup(yytext); return ID;  }
"="			{ yylval.c=strdup(yytext); return E_ASSIGN_OP; }
"-="                    { yylval.c=strdup(yytext); return ASSIGN_OP; }
"+="                    { yylval.c=strdup(yytext); return ASSIGN_OP; }
"<="                    { yylval.c=strdup(yytext); return EQ_OP;   }
">="                    { yylval.c=strdup(yytext); return EQ_OP;}
"=="                    { yylval.c=strdup(yytext); return EQ_OP;       }
"!="                    { yylval.c=strdup(yytext); return EQ_OP;    }
"&&"                    { yylval.c=strdup(yytext); return COND_OP;         }
"||"                    { yylval.c=strdup(yytext); return COND_OP;          }
{REL_OP}                { yylval.c=strdup(yytext); return REL_OP;  }
{ARITH_OP}              { yylval.c=strdup(yytext); return ARITH_OP; }
"-"			{ yylval.c=strdup(yytext); return MINUS ; }

%%
