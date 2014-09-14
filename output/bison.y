%token CLASS Program ID INT_LITERAL VOID INT BOOLEAN IF ELSE FOR E_ASSIGN_OP RETURN BREAK CONTINUE ASSIGN_OP CALLOUT STRING_LITERAL ARITH_OP MINUS REL_OP EQ_OP COND_OP TRUE FALSE CHAR_LITERAL 
%error-verbose
%union {
 int a;
float b;
char *c;
}
%{
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
%}%{
char *s;
%}
%%
program	:
				 CLASS Program '{' field_decl '}' 
	{printf("<<<program: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s;}
				;
field_decl	:
				 type  fields ';' field_decl 	{s=malloc(sizeof(char)*20);sprintf(s," <<<field_decl: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				| method_decl
	{$<c>$=$<c>1;}
				;
fields	:
				 field 	{$<c>$=$<c>1;}
				| field ',' fields 
	{s=malloc(sizeof(char)*15);sprintf(s," <<<fields: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				;
field	:
				 ID  	{$<c>$=$<c>1;}
				| ID  '[' INT_LITERAL  ']' 
	{s=malloc(sizeof(char)*20);sprintf(s," <<<field: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				;
method_decl	:
				 type ID  '(' args_decl ')' block method_decl 	{s=malloc(sizeof(char)*35);sprintf(s," <<<method_decl: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s;}
				| VOID ID  '(' args_decl ')' block method_decl 	{s=malloc(sizeof(char)*35);sprintf(s," <<<method_decl: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s;}
				| 	
	{$<c>$="EMPTY";}
				;
args_decl	:
				 type ID  	{s=malloc(sizeof(char)*10);sprintf(s," <<<args_decl: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| type ID ',' args_decl  	{s=malloc(sizeof(char)*20);sprintf(s," <<<args_decl: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				| 
	{$<c>$="EMPTY";}
				;
vars	:
				 ID ';'  	{s=malloc(sizeof(char)*10);sprintf(s," <<<vars: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| ID ',' vars
	{s=malloc(sizeof(char)*15);sprintf(s," <<<vars: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				;
var_decl	:
				 type vars var_decl	 	{s=malloc(sizeof(char)*15);sprintf(s," <<<var_decl: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| type vars
	{s=malloc(sizeof(char)*10);sprintf(s," <<<var_decl: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				;
block	:
				 '{' block_body '}' 
	{s=malloc(sizeof(char)*15);sprintf(s," <<<block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				;
statements	:
				 statement  	{$<c>$=$<c>1;}
				| statement statements
	{s=malloc(sizeof(char)*10);sprintf(s," <<<statements: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				;
block_body	:
				 var_decl statements		{s=malloc(sizeof(char)*10);sprintf(s," <<<block_body: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
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
				 location ASSGN_OP expr ';'  	{s=malloc(sizeof(char)*20);sprintf(s," <<<statement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				| method_call ';' 	{s=malloc(sizeof(char)*10);sprintf(s," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| IF '(' expr  ')' block  ELSE block	 	{s=malloc(sizeof(char)*35);sprintf(s," <<<statement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s;}
				| IF '(' expr  ')' block   	{s=malloc(sizeof(char)*25);sprintf(s," <<<statement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s;}
				| FOR ID  E_ASSIGN_OP expr ',' expr  block  	{s=malloc(sizeof(char)*35);sprintf(s," <<<statement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s;}
				| RETURN ';' 	{s=malloc(sizeof(char)*10);sprintf(s," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| RETURN expr ';' 	{s=malloc(sizeof(char)*15);sprintf(s," <<<statement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| BREAK ';' 	{s=malloc(sizeof(char)*10);sprintf(s," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| CONTINUE ';'  	{s=malloc(sizeof(char)*10);sprintf(s," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
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
	{s=malloc(sizeof(char)*15);sprintf(s," <<<exprs: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				;
callout_args	:
				 callout_arg  	{$<c>$=$<c>1;}
				| callout_arg ',' callout_args 
	{s=malloc(sizeof(char)*15);sprintf(s," <<<callout_args: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				;
method_call	:
				 method_name '('   ')'	 	{s=malloc(sizeof(char)*15);sprintf(s," <<<method_call: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| method_name '(' exprs ')'      	{s=malloc(sizeof(char)*20);sprintf(s," <<<method_call: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				| CALLOUT '(' STRING_LITERAL ',' callout_args ')'	 	{s=malloc(sizeof(char)*30);sprintf(s," <<<method_call: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s;}
				| CALLOUT '(' STRING_LITERAL  ')' 
	{s=malloc(sizeof(char)*20);sprintf(s," <<<method_call: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				;
method_name	:
				 ID 
	{$<c>$=$<c>1;}
				;
location	:
				 ID		{$<c>$=$<c>1;}
				| ID  '[' expr  ']' 
	{s=malloc(sizeof(char)*20);sprintf(s," <<<location: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s;}
				;
ARTH_OP	:
				 ARITH_OP		{$<c>$=$<c>1;}
				| MINUS
	{$<c>$=$<c>1;}
				;
expr	:
				 expr ARTH_OP term1		{s=malloc(sizeof(char)*15);sprintf(s," <<<expr: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| term1 
	{$<c>$=$<c>1;}
				;
term1	:
				 term1 REL_OP term2    	{s=malloc(sizeof(char)*15);sprintf(s," <<<term1: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| term2 
	{$<c>$=$<c>1;}
				;
term2	:
				 term2 EQ_OP term3     	{s=malloc(sizeof(char)*15);sprintf(s," <<<term2: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| term3 
	{$<c>$=$<c>1;}
				;
term3	:
				 term3 COND_OP term4   	{s=malloc(sizeof(char)*15);sprintf(s," <<<term3: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
				| term4 
	{$<c>$=$<c>1;}
				;
term4	:
				 location		{$<c>$=$<c>1;}
				| method_call		{$<c>$=$<c>1;}
				| literal		{$<c>$=$<c>1;}
				| MINUS term4		{s=malloc(sizeof(char)*10);sprintf(s," <<<term4: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| '!' term4			{s=malloc(sizeof(char)*10);sprintf(s," <<<term4: %s %s >>>",$<c>1,$<c>2);$<c>$=s;}
				| '(' expr  ')' 
	{s=malloc(sizeof(char)*15);sprintf(s," <<<term4: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s;}
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