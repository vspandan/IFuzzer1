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
%}

%%
"class"		{ return (CLASS); }
"program"		{ return (Program); }
"{"		{ return yytext[0]; }
"}"		{ return yytext[0]; }
";"		{ return yytext[0]; }
","		{ return yytext[0]; }
"id"		{ return (ID); }
"["		{ return yytext[0]; }
"int_literal"		{ return (INT_LITERAL); }
"]"		{ return yytext[0]; }
"("		{ return yytext[0]; }
")"		{ return yytext[0]; }
"void"		{ return (VOID); }
"int"		{ return (INT); }
"boolean"		{ return (BOOLEAN); }
"if"		{ return (IF); }
"else"		{ return (ELSE); }
"for"		{ return (FOR); }
"e_assign_op"		{ return (E_ASSIGN_OP); }
"return"		{ return (RETURN); }
"break"		{ return (BREAK); }
"continue"		{ return (CONTINUE); }
"assign_op"		{ return (ASSIGN_OP); }
"callout"		{ return (CALLOUT); }
"string_literal"		{ return (STRING_LITERAL); }
"arith_op"		{ return (ARITH_OP); }
"minus"		{ return (MINUS); }
"rel_op"		{ return (REL_OP); }
"eq_op"		{ return (EQ_OP); }
"cond_op"		{ return (COND_OP); }
"!"		{ return yytext[0]; }
"true"		{ return (TRUE); }
"false"		{ return (FALSE); }
"char_literal"		{ return (CHAR_LITERAL); }
{STRING} 		{ return STRING_LITERAL; }
{INTEGER}		{ return INT_LITERAL; }
{DOUBLE}		{ return INT_LITERAL; }
{HEX_INTEGER}     	{ return INT_LITERAL; }
{IDENTIFIER}            { return ID;  }
"="			{ return E_ASSIGN_OP; }
"-="                    { return ASSIGN_OP; }
"+="                    { return ASSIGN_OP; }
"<="                    { return EQ_OP;   }
">="                    { return EQ_OP;}
"=="                    { return EQ_OP;       }
"!="                    { return EQ_OP;    }
"&&"                    { return COND_OP;         }
"||"                    { return COND_OP;          }
{REL_OP}                { return REL_OP;  }
{ARITH_OP}              { return ARITH_OP; }
"-"			{ return MINUS ; }

%%
