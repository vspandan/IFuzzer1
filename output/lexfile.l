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
"'{'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'}'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"','"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'='"		{ yylval.c=strdup(yytext); return yytext[0]; }
"';'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'('"		{ yylval.c=strdup(yytext); return yytext[0]; }
"')'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"':'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'['"		{ yylval.c=strdup(yytext); return yytext[0]; }
"']'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'.'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"++"		{ yylval.c=strdup("++"); return "++" }
"--"		{ yylval.c=strdup("--"); return "--" }
"'+'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'-'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'~'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'!'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'*'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'/'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'%'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"<<"		{ yylval.c=strdup("<<"); return "<<" }
">>"		{ yylval.c=strdup(">>"); return ">>" }
">>>"		{ yylval.c=strdup(">>>"); return ">>>" }
"'<'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'>'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"<="		{ yylval.c=strdup("<="); return "<=" }
">="		{ yylval.c=strdup(">="); return ">=" }
"=="		{ yylval.c=strdup("=="); return "==" }
"!="		{ yylval.c=strdup("!="); return "!=" }
"==="		{ yylval.c=strdup("==="); return "===" }
"!=="		{ yylval.c=strdup("!=="); return "!==" }
"'&'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"'^'"		{ yylval.c=strdup(yytext); return yytext[0]; }
"&&"		{ yylval.c=strdup("&&"); return "&&" }
"'?'"		{ yylval.c=strdup(yytext); return yytext[0]; }
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
"int_literal"		{ yylval.c=strdup(yytext); return (INT_LITERAL); }
"string_literal"		{ yylval.c=strdup(yytext); return (STRING_LITERAL); }
"null"		{ yylval.c=strdup(yytext); return (null); }
"true"		{ yylval.c=strdup(yytext); return (true); }
"false"		{ yylval.c=strdup(yytext); return (false); }
"class"		{ yylval.c=strdup(yytext); return (Class); }
"enum"		{ yylval.c=strdup(yytext); return (Enum); }
"extends"		{ yylval.c=strdup(yytext); return (Extends); }
"super"		{ yylval.c=strdup(yytext); return (Super); }
"const"		{ yylval.c=strdup(yytext); return (Const); }
"export"		{ yylval.c=strdup(yytext); return (Export); }
"import"		{ yylval.c=strdup(yytext); return (Import); }
"implements"		{ yylval.c=strdup(yytext); return (Implements); }
"let"		{ yylval.c=strdup(yytext); return (Let); }
"private"		{ yylval.c=strdup(yytext); return (Private); }
"public"		{ yylval.c=strdup(yytext); return (Public); }
"interface"		{ yylval.c=strdup(yytext); return (Interface); }
"package"		{ yylval.c=strdup(yytext); return (Package); }
"protected"		{ yylval.c=strdup(yytext); return (Protected); }
"static"		{ yylval.c=strdup(yytext); return (Static); }
"yield"		{ yylval.c=strdup(yytext); return (Yield); }
"semicolon"		{ yylval.c=strdup(yytext); return (SemiColon); }
"break"		{ yylval.c=strdup(yytext); return (break); }
"do"		{ yylval.c=strdup(yytext); return (do); }
"instanceof"		{ yylval.c=strdup(yytext); return (instanceof); }
"typeof"		{ yylval.c=strdup(yytext); return (typeof); }
"case"		{ yylval.c=strdup(yytext); return (case); }
"else"		{ yylval.c=strdup(yytext); return (else); }
"new"		{ yylval.c=strdup(yytext); return (new); }
"var"		{ yylval.c=strdup(yytext); return (var); }
"catch"		{ yylval.c=strdup(yytext); return (catch); }
"finally"		{ yylval.c=strdup(yytext); return (finally); }
"return"		{ yylval.c=strdup(yytext); return (return); }
"void"		{ yylval.c=strdup(yytext); return (void); }
"continue"		{ yylval.c=strdup(yytext); return (continue); }
"for"		{ yylval.c=strdup(yytext); return (for); }
"switch"		{ yylval.c=strdup(yytext); return (switch); }
"while"		{ yylval.c=strdup(yytext); return (while); }
"debugger"		{ yylval.c=strdup(yytext); return (debugger); }
"function"		{ yylval.c=strdup(yytext); return (function); }
"this"		{ yylval.c=strdup(yytext); return (this); }
"with"		{ yylval.c=strdup(yytext); return (with); }
"default"		{ yylval.c=strdup(yytext); return (default); }
"if"		{ yylval.c=strdup(yytext); return (if); }
"throw"		{ yylval.c=strdup(yytext); return (throw); }
"delete"		{ yylval.c=strdup(yytext); return (delete); }
"in"		{ yylval.c=strdup(yytext); return (in); }
"try"		{ yylval.c=strdup(yytext); return (try); }
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
"-"			{ yylval.c=strdup(yytext); return MINUS ; }

%%
