DIGIT		       	[0-9]

HEX_DIGIT  	      	[0-9a-fA-F]
HEX_INTEGER       	0[Xx]{HEX_DIGIT}+
INTEGER           	{DIGIT}+
EXPONENT          	[Ee][-+]?{INTEGER}
DOUBLE          	{INTEGER}"."{DIGIT}*{EXPONENT}?
STRING  	  	\"[^"\n]*\"
IDENTIFIER        	[a-zA-Z][a-zA-Z_0-9]*
ASSIGN_OP          	[=|+=|-=]
ARITH_OP		[-+/*%]
REL_OP			[<|>]
START_COMMENT   	("/*")
END_COMMENT		("*/")
SINGLE_COMMENT  	("//"[^\n]*)
%{

#include<stdio.h>
#include "decaf.tab.h"
%}

%%
"boolean"               { return BOOLEAN; }
"break"                 { return BREAK; }
"callout"               { return CALLOUT; }
"class"                 { return CLASS; }
"true"                  { return TRUE;       }
"false"                 { return FALSE;        }
"for"                   { return FOR;         }
"if"                    { return IF;          }
"else"                  { return ELSE;        }
"return"                { return RETURN;      }
"void"                  { return VOID;         }
"int"                   { return INT;         }
{STRING}        { return STRING_LITERAL; }
(INTEGER|DOUBLE|HEX_INTEGER)     { return INT_LITERAL; }
{IDENTIFIER}            { return ID;  }
"<="                    { return EQ_OP;   }
">="                    { return EQ_OP;}
"=="                    { return EQ_OP;       }
"!="                    { return EQ_OP;    }
"&&"                    { return COND_OP;         }
"||"                    { return COND_OP;          }
{REL_OP}                { return yytext[0];  }
{ARITH_OP}              { return yytext[0]; }
"{"			{ return yytext[0] ;}
"}"			{ return yytext[0] ; }
";"			{ return yytext[0] ;}
"["                     { return yytext[0] ;}
"]"                     { return yytext[0] ;}
"("                     { return yytext[0] ;}
")"                     { return yytext[0] ;}
"!"			{ return yytext[0] ;}
%%


