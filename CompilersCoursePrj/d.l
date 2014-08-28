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

%%
"boolean"    		{ printf("return boolean");  }
"break"           	{ printf("return Break");       }
"callout"         	{ printf("return Callout");       }
"class"           	{ printf("return Class");       }
"true"          	{ printf("return True");       }
"false"            	{ printf("return False");        }
"for"               	{ printf("return For");         }
"if"                	{ printf("return If");          }
"else"             	{ printf("return Else");        }
"return"          	{ printf("return Return");      }
"void"             	{ printf("return Void");         }
"int"               	{ printf("return Int");         }
{IDENTIFIER}            { printf("return Identifier"); }
"<="                	{ printf("return LessEqual");   }
">="                	{ printf("return GreaterEqual");}
"=="                	{ printf("return Equal");       }
"!="                	{ printf("return NotEqual");    }
"&&"               	{ printf("return And");         }
"||"                	{ printf("return Or");          }
{REL_OP}    		{ printf("%c", yytext[0]);  }
{ARITH_OP}    		{ printf("%c",yytext[0]); }
"[]"                	{ printf("return T_Dims");      }
%%
main()
{

yylex();
}
