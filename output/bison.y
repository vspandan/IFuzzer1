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
%}
%{
char *s;
%}
%%
program	:
				 CLASS Program '{' field_decl '}' 
	{printf("<<<program: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);}
				;
field_decl	:
				 type  fields ';' field_decl 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+14 ;char *s2=malloc(sizeof(char)*len);sprintf(s2," <<<field_decl: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s2;}
				| method_decl
	{$<c>$=$<c>1;}
				;
fields	:
				 field 	{$<c>$=$<c>1;}
				| field ',' fields 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+9 ;char *s5=malloc(sizeof(char)*len);sprintf(s5," <<<fields: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s5;}
				;
field	:
				 ID  	{$<c>$=$<c>1;}
				| ID  '[' INT_LITERAL  ']' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+9 ;char *s7=malloc(sizeof(char)*len);sprintf(s7," <<<field: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s7;}
				;
method_decl	:
				 type ID  '(' args_decl ')' block method_decl 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+18 ;char *s8=malloc(sizeof(char)*len);sprintf(s8," <<<method_decl: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s8;}
				| VOID ID  '(' args_decl ')' block method_decl 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+18 ;char *s9=malloc(sizeof(char)*len);sprintf(s9," <<<method_decl: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s9;}
				| 	
	{$<c>$="EMPTY";}
				;
args_decl	:
				 type ID  	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s11=malloc(sizeof(char)*len);sprintf(s11," <<<args_decl: %s %s >>>",$<c>1,$<c>2);$<c>$=s11;}
				| type ID ',' args_decl  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s12=malloc(sizeof(char)*len);sprintf(s12," <<<args_decl: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s12;}
				| 
	{$<c>$="EMPTY";}
				;
vars	:
				 ID ';'  	{int len=strlen($<c>1)+strlen($<c>2)+7+6 ;char *s14=malloc(sizeof(char)*len);sprintf(s14," <<<vars: %s %s >>>",$<c>1,$<c>2);$<c>$=s14;}
				| ID ',' vars
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+7 ;char *s15=malloc(sizeof(char)*len);sprintf(s15," <<<vars: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s15;}
				;
var_decl	:
				 type vars var_decl	 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+11 ;char *s16=malloc(sizeof(char)*len);sprintf(s16," <<<var_decl: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s16;}
				| type vars
	{int len=strlen($<c>1)+strlen($<c>2)+7+10 ;char *s17=malloc(sizeof(char)*len);sprintf(s17," <<<var_decl: %s %s >>>",$<c>1,$<c>2);$<c>$=s17;}
				;
block	:
				 '{' block_body '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s18=malloc(sizeof(char)*len);sprintf(s18," <<<block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s18;}
				;
statements	:
				 statement  	{$<c>$=$<c>1;}
				| statement statements
	{int len=strlen($<c>1)+strlen($<c>2)+7+12 ;char *s20=malloc(sizeof(char)*len);sprintf(s20," <<<statements: %s %s >>>",$<c>1,$<c>2);$<c>$=s20;}
				;
block_body	:
				 var_decl statements		{int len=strlen($<c>1)+strlen($<c>2)+7+12 ;char *s21=malloc(sizeof(char)*len);sprintf(s21," <<<block_body: %s %s >>>",$<c>1,$<c>2);$<c>$=s21;}
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
				 location ASSGN_OP expr ';'  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s27=malloc(sizeof(char)*len);sprintf(s27," <<<statement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s27;}
				| method_call ';' 	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s28=malloc(sizeof(char)*len);sprintf(s28," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s28;}
				| IF '(' expr  ')' block  ELSE block	 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+16 ;char *s29=malloc(sizeof(char)*len);sprintf(s29," <<<statement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s29;}
				| IF '(' expr  ')' block   	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+14 ;char *s30=malloc(sizeof(char)*len);sprintf(s30," <<<statement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s30;}
				| FOR ID  E_ASSIGN_OP expr ',' expr  block  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+16 ;char *s31=malloc(sizeof(char)*len);sprintf(s31," <<<statement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s31;}
				| RETURN ';' 	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s32=malloc(sizeof(char)*len);sprintf(s32," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s32;}
				| RETURN expr ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s33=malloc(sizeof(char)*len);sprintf(s33," <<<statement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s33;}
				| BREAK ';' 	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s34=malloc(sizeof(char)*len);sprintf(s34," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s34;}
				| CONTINUE ';'  	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<statement: %s %s >>>",$<c>1,$<c>2);$<c>$=s35;}
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
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<exprs: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s40;}
				;
callout_args	:
				 callout_arg  	{$<c>$=$<c>1;}
				| callout_arg ',' callout_args 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<callout_args: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s42;}
				;
method_call	:
				 method_name '('   ')'	 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+14 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<method_call: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s43;}
				| method_name '(' exprs ')'      	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+15 ;char *s44=malloc(sizeof(char)*len);sprintf(s44," <<<method_call: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s44;}
				| CALLOUT '(' STRING_LITERAL ',' callout_args ')'	 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+17 ;char *s45=malloc(sizeof(char)*len);sprintf(s45," <<<method_call: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s45;}
				| CALLOUT '(' STRING_LITERAL  ')' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+15 ;char *s46=malloc(sizeof(char)*len);sprintf(s46," <<<method_call: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s46;}
				;
method_name	:
				 ID 
	{$<c>$=$<c>1;}
				;
location	:
				 ID		{$<c>$=$<c>1;}
				| ID  '[' expr  ']' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+12 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<location: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s49;}
				;
ARTH_OP	:
				 ARITH_OP		{$<c>$=$<c>1;}
				| MINUS
	{$<c>$=$<c>1;}
				;
expr	:
				 expr ARTH_OP term1		{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+7 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<expr: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s52;}
				| term1 
	{$<c>$=$<c>1;}
				;
term1	:
				 term1 REL_OP term2    	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<term1: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s54;}
				| term2 
	{$<c>$=$<c>1;}
				;
term2	:
				 term2 EQ_OP term3     	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s56=malloc(sizeof(char)*len);sprintf(s56," <<<term2: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s56;}
				| term3 
	{$<c>$=$<c>1;}
				;
term3	:
				 term3 COND_OP term4   	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<term3: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s58;}
				| term4 
	{$<c>$=$<c>1;}
				;
term4	:
				 location		{$<c>$=$<c>1;}
				| method_call		{$<c>$=$<c>1;}
				| literal		{$<c>$=$<c>1;}
				| MINUS term4		{int len=strlen($<c>1)+strlen($<c>2)+7+7 ;char *s63=malloc(sizeof(char)*len);sprintf(s63," <<<term4: %s %s >>>",$<c>1,$<c>2);$<c>$=s63;}
				| '!' term4			{int len=strlen($<c>1)+strlen($<c>2)+7+7 ;char *s64=malloc(sizeof(char)*len);sprintf(s64," <<<term4: %s %s >>>",$<c>1,$<c>2);$<c>$=s64;}
				| '(' expr  ')' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<term4: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s65;}
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