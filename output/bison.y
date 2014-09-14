%token CLASS Program ID INT_LITERAL VOID INT BOOLEAN IF ELSE FOR E_ASSIGN_OP RETURN BREAK CONTINUE ASSIGN_OP CALLOUT STRING_LITERAL ARITH_OP MINUS REL_OP EQ_OP COND_OP TRUE FALSE CHAR_LITERAL 
%error-verbose
%union {
 int a;
float b;
char *c;
}
%{
#include <stdlib.h>
%}
%{
#include <stdio.h>
%}
%{
#include <string.h>
%}
%%
program	:
				 CLASS Program '{' field_decl '}' 
	{printf("<<<program %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);}
				;
field_decl	:
				 type  fields ';' field_decl 	{sprintf($<c>$," <<<field_decl %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| method_decl
	{$<c>$=$<c>1;}
				;
fields	:
				 field 	{$<c>$=$<c>1;}
				| field ',' fields 
	{sprintf($<c>$," <<<fields %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
field	:
				 ID  	{$<c>$=$<c>1;}
				| ID  '[' INT_LITERAL  ']' 
	{sprintf($<c>$," <<<field %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
method_decl	:
				 type ID  '(' args_decl ')' block method_decl 	{sprintf($<c>$," <<<method_decl %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| VOID ID  '(' args_decl ')' block method_decl 	{sprintf($<c>$," <<<method_decl %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| 	
	{$<c>$="EMPTY";}
				;
args_decl	:
				 type ID  	{sprintf($<c>$," <<<args_decl %s %s >>>",$<c>1,$<c>2);}
				| type ID ',' args_decl  	{sprintf($<c>$," <<<args_decl %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| 
	{$<c>$="EMPTY";}
				;
vars	:
				 ID ';'  	{sprintf($<c>$," <<<vars %s %s >>>",$<c>1,$<c>2);}
				| ID ',' vars
	{sprintf($<c>$," <<<vars %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
var_decl	:
				 type vars var_decl	 	{sprintf($<c>$," <<<var_decl %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| type vars
	{sprintf($<c>$," <<<var_decl %s %s >>>",$<c>1,$<c>2);}
				;
block	:
				 '{' block_body '}' 
	{sprintf($<c>$," <<<block %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
statements	:
				 statement  	{$<c>$=$<c>1;}
				| statement statements
	{sprintf($<c>$," <<<statements %s %s >>>",$<c>1,$<c>2);}
				;
block_body	:
				 var_decl statements		{sprintf($<c>$," <<<block_body %s %s >>>",$<c>1,$<c>2);}
				| var_decl   	{$<c>$=$<c>1;}
				| statements		{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
type	:
				 INT 	{$<c>$=$<c>1;}
				| BOOLEAN 
	{$<c>$=$<c>1;}
				;
statement	:
				 location ASSGN_OP expr ';'  	{sprintf($<c>$," <<<statement %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| method_call ';' 	{sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| IF '(' expr  ')' block  ELSE block	 	{sprintf($<c>$," <<<statement %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| IF '(' expr  ')' block   	{sprintf($<c>$," <<<statement %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);}
				| FOR ID  E_ASSIGN_OP expr ',' expr  block  	{sprintf($<c>$," <<<statement %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| RETURN ';' 	{sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| RETURN expr ';' 	{sprintf($<c>$," <<<statement %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| BREAK ';' 	{sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| CONTINUE ';'  	{sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| block 
	{$<c>$=$<c>1;}
				;
ASSGN_OP	:
				 ASSIGN_OP 	{$<c>$=$<c>1;}
				| E_ASSIGN_OP 
	{$<c>$=$<c>1;}
				;
exprs	:
				 expr		{$<c>$=$<c>1;}
				| expr ',' exprs 
	{sprintf($<c>$," <<<exprs %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
callout_args	:
				 callout_arg  	{$<c>$=$<c>1;}
				| callout_arg ',' callout_args 
	{sprintf($<c>$," <<<callout_args %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
method_call	:
				 method_name '('   ')'	 	{sprintf($<c>$," <<<method_call %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| method_name '(' exprs ')'      	{sprintf($<c>$," <<<method_call %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| CALLOUT '(' STRING_LITERAL ',' callout_args ')'	 	{sprintf($<c>$," <<<method_call %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);}
				| CALLOUT '(' STRING_LITERAL  ')' 
	{sprintf($<c>$," <<<method_call %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
method_name	:
				 ID 
	{$<c>$=$<c>1;}
				;
location	:
				 ID		{$<c>$=$<c>1;}
				| ID  '[' expr  ']' 
	{sprintf($<c>$," <<<location %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
ARTH_OP	:
				 ARITH_OP		{$<c>$=$<c>1;}
				| MINUS
	{$<c>$=$<c>1;}
				;
expr	:
				 expr ARTH_OP term1		{sprintf($<c>$," <<<expr %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term1 
	{$<c>$=$<c>1;}
				;
term1	:
				 term1 REL_OP term2    	{sprintf($<c>$," <<<term1 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term2 
	{$<c>$=$<c>1;}
				;
term2	:
				 term2 EQ_OP term3     	{sprintf($<c>$," <<<term2 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term3 
	{$<c>$=$<c>1;}
				;
term3	:
				 term3 COND_OP term4   	{sprintf($<c>$," <<<term3 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term4 
	{$<c>$=$<c>1;}
				;
term4	:
				 location		{$<c>$=$<c>1;}
				| method_call		{$<c>$=$<c>1;}
				| literal		{$<c>$=$<c>1;}
				| MINUS term4		{sprintf($<c>$," <<<term4 %s %s >>>",$<c>1,$<c>2);}
				| '!' term4			{sprintf($<c>$," <<<term4 %s %s >>>",$<c>1,$<c>2);}
				| '(' expr  ')' 
	{sprintf($<c>$," <<<term4 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
callout_arg	:
				 expr		{$<c>$=$<c>1;}
				| STRING_LITERAL
	{$<c>$=$<c>1;}
				;
bool_literal	:
				 TRUE 		{$<c>$=$<c>1;}
				| FALSE
	{$<c>$=$<c>1;}
				;
literal	:
				 INT_LITERAL		{$<c>$=$<c>1;}
				| CHAR_LITERAL		{$<c>$=$<c>1;}
				| bool_literal 	{$<c>$=$<c>1;}
				;

%%
int main()
{
yyparse();
}