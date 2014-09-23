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
"{"		{ yylval.c=strdup(yytext); return yytext[0]; }
"}"		{ yylval.c=strdup(yytext); return yytext[0]; }
"var"		{ yylval.c=strdup(yytext); return (Var); }
";"		{ yylval.c=strdup(yytext); return yytext[0]; }
","		{ yylval.c=strdup(yytext); return yytext[0]; }
"="		{ yylval.c=strdup(yytext); return yytext[0]; }
"if"		{ yylval.c=strdup(yytext); return (If); }
"("		{ yylval.c=strdup(yytext); return yytext[0]; }
")"		{ yylval.c=strdup(yytext); return yytext[0]; }
"do"		{ yylval.c=strdup(yytext); return (Do); }
"while"		{ yylval.c=strdup(yytext); return (While); }
"for"		{ yylval.c=strdup(yytext); return (For); }
"in"		{ yylval.c=strdup(yytext); return (In); }
"continue"		{ yylval.c=strdup(yytext); return (Continue); }
"break"		{ yylval.c=strdup(yytext); return (Break); }
"return"		{ yylval.c=strdup(yytext); return (Return); }
"with"		{ yylval.c=strdup(yytext); return (With); }
"switch"		{ yylval.c=strdup(yytext); return (Switch); }
"case"		{ yylval.c=strdup(yytext); return (Case); }
":"		{ yylval.c=strdup(yytext); return yytext[0]; }
"default"		{ yylval.c=strdup(yytext); return (Default); }
"throw"		{ yylval.c=strdup(yytext); return (Throw); }
"try"		{ yylval.c=strdup(yytext); return (Try); }
"catch"		{ yylval.c=strdup(yytext); return (Catch); }
"finally"		{ yylval.c=strdup(yytext); return (Finally); }
"debugger"		{ yylval.c=strdup(yytext); return (Debugger); }
"function"		{ yylval.c=strdup(yytext); return (Function); }
"["		{ yylval.c=strdup(yytext); return yytext[0]; }
"]"		{ yylval.c=strdup(yytext); return yytext[0]; }
"."		{ yylval.c=strdup(yytext); return yytext[0]; }
"new"		{ yylval.c=strdup(yytext); return (New); }
"this"		{ yylval.c=strdup(yytext); return (This); }
"newexpression"		{ yylval.c=strdup(yytext); return (NewExpression); }
"?"		{ yylval.c=strdup(yytext); return yytext[0]; }
"##"		{ yylval.c=strdup("##"); return "##"; }
"&&"		{ yylval.c=strdup("&&"); return "&&"; }
"#"		{ yylval.c=strdup(yytext); return yytext[0]; }
"^"		{ yylval.c=strdup(yytext); return yytext[0]; }
"&"		{ yylval.c=strdup(yytext); return yytext[0]; }
"=="		{ yylval.c=strdup("=="); return "=="; }
"!="		{ yylval.c=strdup("!="); return "!="; }
"==="		{ yylval.c=strdup("==="); return "==="; }
"!=="		{ yylval.c=strdup("!=="); return "!=="; }
"<"		{ yylval.c=strdup(yytext); return yytext[0]; }
">"		{ yylval.c=strdup(yytext); return yytext[0]; }
"<="		{ yylval.c=strdup("<="); return "<="; }
">="		{ yylval.c=strdup(">="); return ">="; }
"instanceof"		{ yylval.c=strdup(yytext); return (Instanceof); }
"<<"		{ yylval.c=strdup("<<"); return "<<"; }
">>"		{ yylval.c=strdup(">>"); return ">>"; }
">>>"		{ yylval.c=strdup(">>>"); return ">>>"; }
"+"		{ yylval.c=strdup(yytext); return yytext[0]; }
"-"		{ yylval.c=strdup(yytext); return yytext[0]; }
"*"		{ yylval.c=strdup(yytext); return yytext[0]; }
"/"		{ yylval.c=strdup(yytext); return yytext[0]; }
"%"		{ yylval.c=strdup(yytext); return yytext[0]; }
"delete"		{ yylval.c=strdup(yytext); return (Delete); }
"void"		{ yylval.c=strdup(yytext); return (Void); }
"typeof"		{ yylval.c=strdup(yytext); return (Typeof); }
"++"		{ yylval.c=strdup("++"); return "++"; }
"--"		{ yylval.c=strdup("--"); return "--"; }
"~"		{ yylval.c=strdup(yytext); return yytext[0]; }
"!"		{ yylval.c=strdup(yytext); return yytext[0]; }
"*="		{ yylval.c=strdup("*="); return "*="; }
"/="		{ yylval.c=strdup("/="); return "/="; }
"%="		{ yylval.c=strdup("%="); return "%="; }
"+="		{ yylval.c=strdup("+="); return "+="; }
"-="		{ yylval.c=strdup("-="); return "-="; }
"<<="		{ yylval.c=strdup("<<="); return "<<="; }
">>="		{ yylval.c=strdup(">>="); return ">>="; }
">>>="		{ yylval.c=strdup(">>>="); return ">>>="; }
"&="		{ yylval.c=strdup("&="); return "&="; }
"^="		{ yylval.c=strdup("^="); return "^="; }
"int_literal"		{ yylval.c=strdup(yytext); return (INT_LITERAL); }
"string_literal"		{ yylval.c=strdup(yytext); return (STRING_LITERAL); }
"null"		{ yylval.c=strdup(yytext); return (null); }
"true"		{ yylval.c=strdup(yytext); return (true); }
"false"		{ yylval.c=strdup(yytext); return (false); }
"id"		{ yylval.c=strdup(yytext); return (ID); }
"assign_op"		{ yylval.c=strdup(yytext); return (ASSIGN_OP); }
"e_assign_op"		{ yylval.c=strdup(yytext); return (E_ASSIGN_OP); }
"char_literal"		{ yylval.c=strdup(yytext); return (CHAR_LITERAL); }
"eq_op"		{ yylval.c=strdup(yytext); return (EQ_OP); }
"cond_op"		{ yylval.c=strdup(yytext); return (COND_OP); }
"rel_op"		{ yylval.c=strdup(yytext); return (REL_OP); }
"arith_op"		{ yylval.c=strdup(yytext); return (ARITH_OP); }
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

%%
