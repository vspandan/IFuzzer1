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
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	printf("<<<program %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);}
				;
field_decl	:
				 type  fields ';' field_decl 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<field_decl %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| method_decl
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<field_decl %s >>>",$<c>1);}
				;
fields	:
				 field 	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<fields %s >>>",$<c>1);}
				| field ',' fields 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<fields %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
field	:
				 ID  	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<field %s >>>",$<c>1);}
				| ID  '[' INT_LITERAL  ']' 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<field %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
method_decl	:
				 type ID  '(' args_decl ')' block method_decl 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	if ($<c>6== '\0')	$<c>6= "@";	if ($<c>7== '\0')	$<c>7= "@";	sprintf($<c>$," <<<method_decl %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| VOID ID  '(' args_decl ')' block method_decl 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	if ($<c>6== '\0')	$<c>6= "@";	if ($<c>7== '\0')	$<c>7= "@";	sprintf($<c>$," <<<method_decl %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| 	

				;
args_decl	:
				 type ID  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<args_decl %s %s >>>",$<c>1,$<c>2);}
				| type ID ',' args_decl  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<args_decl %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| 

				;
vars	:
				 ID ';'  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<vars %s %s >>>",$<c>1,$<c>2);}
				| ID ',' vars
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<vars %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
var_decl	:
				 type vars var_decl	 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<var_decl %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| type vars
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<var_decl %s %s >>>",$<c>1,$<c>2);}
				;
block	:
				 '{' block_body '}' 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<block %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
statements	:
				 statement  	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<statements %s >>>",$<c>1);}
				| statement statements
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<statements %s %s >>>",$<c>1,$<c>2);}
				;
block_body	:
				 var_decl statements		{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<block_body %s %s >>>",$<c>1,$<c>2);}
				| var_decl   	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<block_body %s >>>",$<c>1);}
				| statements		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<block_body %s >>>",$<c>1);}
				| 

				;
type	:
				 INT 	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<type %s >>>",$<c>1);}
				| BOOLEAN 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<type %s >>>",$<c>1);}
				;
statement	:
				 location ASSGN_OP expr ';'  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<statement %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| method_call ';' 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| IF '(' expr  ')' block  ELSE block	 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	if ($<c>6== '\0')	$<c>6= "@";	if ($<c>7== '\0')	$<c>7= "@";	sprintf($<c>$," <<<statement %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| IF '(' expr  ')' block   	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	sprintf($<c>$," <<<statement %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);}
				| FOR ID  E_ASSIGN_OP expr ',' expr  block  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	if ($<c>6== '\0')	$<c>6= "@";	if ($<c>7== '\0')	$<c>7= "@";	sprintf($<c>$," <<<statement %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);}
				| RETURN ';' 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| RETURN expr ';' 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<statement %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| BREAK ';' 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| CONTINUE ';'  	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<statement %s %s >>>",$<c>1,$<c>2);}
				| block 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<statement %s >>>",$<c>1);}
				;
ASSGN_OP	:
				 ASSIGN_OP 	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<ASSGN_OP %s >>>",$<c>1);}
				| E_ASSIGN_OP 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<ASSGN_OP %s >>>",$<c>1);}
				;
exprs	:
				 expr		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<exprs %s >>>",$<c>1);}
				| expr ',' exprs 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<exprs %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
callout_args	:
				 callout_arg  	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<callout_args %s >>>",$<c>1);}
				| callout_arg ',' callout_args 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<callout_args %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
method_call	:
				 method_name '('   ')'	 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<method_call %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| method_name '(' exprs ')'      	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<method_call %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				| CALLOUT '(' STRING_LITERAL ',' callout_args ')'	 	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	if ($<c>5== '\0')	$<c>5= "@";	if ($<c>6== '\0')	$<c>6= "@";	sprintf($<c>$," <<<method_call %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);}
				| CALLOUT '(' STRING_LITERAL  ')' 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<method_call %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
method_name	:
				 ID 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<method_name %s >>>",$<c>1);}
				;
location	:
				 ID		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<location %s >>>",$<c>1);}
				| ID  '[' expr  ']' 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	if ($<c>4== '\0')	$<c>4= "@";	sprintf($<c>$," <<<location %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);}
				;
ARTH_OP	:
				 ARITH_OP		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<ARTH_OP %s >>>",$<c>1);}
				| MINUS
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<ARTH_OP %s >>>",$<c>1);}
				;
expr	:
				 expr ARTH_OP term1		{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<expr %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term1 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<expr %s >>>",$<c>1);}
				;
term1	:
				 term1 REL_OP term2    	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<term1 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term2 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term1 %s >>>",$<c>1);}
				;
term2	:
				 term2 EQ_OP term3     	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<term2 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term3 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term2 %s >>>",$<c>1);}
				;
term3	:
				 term3 COND_OP term4   	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<term3 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				| term4 
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term3 %s >>>",$<c>1);}
				;
term4	:
				 location		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term4 %s >>>",$<c>1);}
				| method_call		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term4 %s >>>",$<c>1);}
				| literal		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<term4 %s >>>",$<c>1);}
				| MINUS term4		{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<term4 %s %s >>>",$<c>1,$<c>2);}
				| '!' term4			{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	sprintf($<c>$," <<<term4 %s %s >>>",$<c>1,$<c>2);}
				| '(' expr  ')' 
	{if ($<c>1== '\0')	$<c>1= "@";	if ($<c>2== '\0')	$<c>2= "@";	if ($<c>3== '\0')	$<c>3= "@";	sprintf($<c>$," <<<term4 %s %s %s >>>",$<c>1,$<c>2,$<c>3);}
				;
callout_arg	:
				 expr		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<callout_arg %s >>>",$<c>1);}
				| STRING_LITERAL
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<callout_arg %s >>>",$<c>1);}
				;
bool_literal	:
				 TRUE 		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<bool_literal %s >>>",$<c>1);}
				| FALSE
	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<bool_literal %s >>>",$<c>1);}
				;
literal	:
				 INT_LITERAL		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<literal %s >>>",$<c>1);}
				| CHAR_LITERAL		{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<literal %s >>>",$<c>1);}
				| bool_literal 	{if ($<c>1== '\0')	$<c>1= "@";	sprintf($<c>$," <<<literal %s >>>",$<c>1);}
				;

%%
int main()
{
yyparse();
}