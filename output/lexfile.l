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
"this"		{ yylval.c=strdup(yytext); return (this); }
"identifier"		{ yylval.c=strdup(yytext); return (Identifier); }
"literal"		{ yylval.c=strdup(yytext); return (Literal); }
"("		{ yylval.c=strdup(yytext); return yytext[0]; }
")"		{ yylval.c=strdup(yytext); return yytext[0]; }
"["		{ yylval.c=strdup(yytext); return yytext[0]; }
"]"		{ yylval.c=strdup(yytext); return yytext[0]; }
","		{ yylval.c=strdup(yytext); return yytext[0]; }
"{"		{ yylval.c=strdup(yytext); return yytext[0]; }
"}"		{ yylval.c=strdup(yytext); return yytext[0]; }
":"		{ yylval.c=strdup(yytext); return yytext[0]; }
"get"PropertyName		{ yylval.c=strdup("get"PropertyName); return "get"PropertyName }
"set"PropertyName		{ yylval.c=strdup("set"PropertyName); return "set"PropertyName }
"numericliteral"		{ yylval.c=strdup(yytext); return (NumericLiteral); }
"stringliteral"		{ yylval.c=strdup(yytext); return (StringLiteral); }
"."		{ yylval.c=strdup(yytext); return yytext[0]; }
"new"		{ yylval.c=strdup(yytext); return (new); }
"delete"		{ yylval.c=strdup(yytext); return (delete); }
"void"		{ yylval.c=strdup(yytext); return (void); }
"typeof"		{ yylval.c=strdup(yytext); return (typeof); }
"++"		{ yylval.c=strdup("++"); return "++" }
"--"		{ yylval.c=strdup("--"); return "--" }
"+"		{ yylval.c=strdup(yytext); return yytext[0]; }
"-"		{ yylval.c=strdup(yytext); return yytext[0]; }
"~"		{ yylval.c=strdup(yytext); return yytext[0]; }
"!"		{ yylval.c=strdup(yytext); return yytext[0]; }
"*"		{ yylval.c=strdup(yytext); return yytext[0]; }
"/"		{ yylval.c=strdup(yytext); return yytext[0]; }
"%"		{ yylval.c=strdup(yytext); return yytext[0]; }
"<<"		{ yylval.c=strdup("<<"); return "<<" }
">>"		{ yylval.c=strdup(">>"); return ">>" }
">>>"		{ yylval.c=strdup(">>>"); return ">>>" }
"<"		{ yylval.c=strdup(yytext); return yytext[0]; }
">"		{ yylval.c=strdup(yytext); return yytext[0]; }
"<="		{ yylval.c=strdup("<="); return "<=" }
">="		{ yylval.c=strdup(">="); return ">=" }
"instanceof"		{ yylval.c=strdup(yytext); return (instanceof); }
"in"		{ yylval.c=strdup(yytext); return (in); }
"=="		{ yylval.c=strdup("=="); return "==" }
"!="		{ yylval.c=strdup("!="); return "!=" }
"==="		{ yylval.c=strdup("==="); return "===" }
"!=="		{ yylval.c=strdup("!=="); return "!==" }
"&"		{ yylval.c=strdup(yytext); return yytext[0]; }
"^"		{ yylval.c=strdup(yytext); return yytext[0]; }
"#"		{ yylval.c=strdup(yytext); return yytext[0]; }
"&&"		{ yylval.c=strdup("&&"); return "&&" }
"##"		{ yylval.c=strdup("##"); return "##" }
"?"		{ yylval.c=strdup(yytext); return yytext[0]; }
"="		{ yylval.c=strdup(yytext); return yytext[0]; }
"*="		{ yylval.c=strdup("*="); return "*=" }
"/="		{ yylval.c=strdup("/="); return "/=" }
"%="		{ yylval.c=strdup("%="); return "%=" }
"+="		{ yylval.c=strdup("+="); return "+=" }
"-="		{ yylval.c=strdup("-="); return "-=" }
"<<="		{ yylval.c=strdup("<<="); return "<<=" }
">>="		{ yylval.c=strdup(">>="); return ">>=" }
">>>="		{ yylval.c=strdup(">>>="); return ">>>=" }
"&="		{ yylval.c=strdup("&="); return "&=" }
"^="		{ yylval.c=strdup("^="); return "^=" }
"var"		{ yylval.c=strdup(yytext); return (var); }
";"		{ yylval.c=strdup(yytext); return yytext[0]; }
"if"		{ yylval.c=strdup(yytext); return (if); }
"else"		{ yylval.c=strdup(yytext); return (else); }
"do"		{ yylval.c=strdup(yytext); return (do); }
"while"		{ yylval.c=strdup(yytext); return (while); }
"for"		{ yylval.c=strdup(yytext); return (for); }
"continue"		{ yylval.c=strdup(yytext); return (continue); }
"break"		{ yylval.c=strdup(yytext); return (break); }
"return"		{ yylval.c=strdup(yytext); return (return); }
"with"		{ yylval.c=strdup(yytext); return (with); }
"switch"		{ yylval.c=strdup(yytext); return (switch); }
"case"		{ yylval.c=strdup(yytext); return (case); }
"default"		{ yylval.c=strdup(yytext); return (default); }
"throw"		{ yylval.c=strdup(yytext); return (throw); }
"try"		{ yylval.c=strdup(yytext); return (try); }
"catch"		{ yylval.c=strdup(yytext); return (catch); }
"finally"		{ yylval.c=strdup(yytext); return (finally); }
"block"		{ yylval.c=strdup(yytext); return (block); }
"debugger"		{ yylval.c=strdup(yytext); return (debugger); }
"function"		{ yylval.c=strdup(yytext); return (function); }
"assign_op"		{ yylval.c=strdup(yytext); return (ASSIGN_OP); }
"int_literal"		{ yylval.c=strdup(yytext); return (INT_LITERAL); }
"string_literal"		{ yylval.c=strdup(yytext); return (STRING_LITERAL); }
"id"		{ yylval.c=strdup(yytext); return (ID); }
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
"-"			{ yylval.c=strdup(yytext); return MINUS ; }

%%
