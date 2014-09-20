%token var if else do while for in continue break return with switch case default throw try catch finally debugger function new Arguments this identifier instanceof delete void UnaryExpression typeof INT_LITERAL STRING_LITERAL null true false ID ASSIGN_OP E_ASSIGN_OP CHAR_LITERAL EQ_OP COND_OP REL_OP ARITH_OP 

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
				 sourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
sourceElements	:
				 sourceElement 	{$<c>$=$<c>1;}
				| sourceElements sourceElement
	{printf("<<<sourceElements: %s %s >>>",$<c>1,$<c>2);}
				;
sourceElement	:
				 statement 	{$<c>$=$<c>1;}
				| functionDeclaration
	{$<c>$=$<c>1;}
				;
statement	:
				 block 	{$<c>$=$<c>1;}
				| variableStatement 	{$<c>$=$<c>1;}
				| emptyStatement 	{$<c>$=$<c>1;}
				| expression 	{$<c>$=$<c>1;}
				| ifStatement 	{$<c>$=$<c>1;}
				| iterationStatement 	{$<c>$=$<c>1;}
				| continueStatement 	{$<c>$=$<c>1;}
				| breakStatement 	{$<c>$=$<c>1;}
				| returnStatement 	{$<c>$=$<c>1;}
				| withStatement 	{$<c>$=$<c>1;}
				| labelledStatement 	{$<c>$=$<c>1;}
				| switchStatement 	{$<c>$=$<c>1;}
				| throwStatement 	{$<c>$=$<c>1;}
				| tryStatement 	{$<c>$=$<c>1;}
				| debuggerStatement
	{$<c>$=$<c>1;}
				;
block	:
				 '{' statementList '}'	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s22=malloc(sizeof(char)*len);sprintf(s22," <<<block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s22;}
				| empty
	{$<c>$=$<c>1;}
				;
empty	:
				 '{' '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+7 ;char *s24=malloc(sizeof(char)*len);sprintf(s24," <<<empty: %s %s >>>",$<c>1,$<c>2);$<c>$=s24;}
				;
statementList	:
				 statement 	{$<c>$=$<c>1;}
				| statementList statement
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s26=malloc(sizeof(char)*len);sprintf(s26," <<<statementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s26;}
				;
variableStatement	:
				 var variableDeclarationList ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s27=malloc(sizeof(char)*len);sprintf(s27," <<<variableStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s27;}
				;
variableDeclarationList	:
				 variableDeclarationList  ',' variableDeclaration 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+26 ;char *s28=malloc(sizeof(char)*len);sprintf(s28," <<<variableDeclarationList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s28;}
				| variableDeclaration
	{$<c>$=$<c>1;}
				;
variableDeclaration	:
				 Identifier  	{$<c>$=$<c>1;}
				| Identifier initialiser 
	{int len=strlen($<c>1)+strlen($<c>2)+7+21 ;char *s31=malloc(sizeof(char)*len);sprintf(s31," <<<variableDeclaration: %s %s >>>",$<c>1,$<c>2);$<c>$=s31;}
				;
initialiser	:
				 '=' assignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s32=malloc(sizeof(char)*len);sprintf(s32," <<<initialiser: %s %s >>>",$<c>1,$<c>2);$<c>$=s32;}
				;
emptyStatement	:
				 ';'
	{$<c>$=$<c>1;}
				;
ifStatement	:
				 if '(' expression ')' statement else statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+18 ;char *s34=malloc(sizeof(char)*len);sprintf(s34," <<<ifStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s34;}
				| if '(' expression ')' statement   
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+16 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<ifStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s35;}
				;
iterationStatement	:
				 do statement while '(' expression ')' ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s36=malloc(sizeof(char)*len);sprintf(s36," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s36;}
				| while '(' expression ')' statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+23 ;char *s37=malloc(sizeof(char)*len);sprintf(s37," <<<iterationStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s37;}
				| for '(' expression ';' expression ';' expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s38=malloc(sizeof(char)*len);sprintf(s38," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s38;}
				| for '(' ';' expression ';' expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s39=malloc(sizeof(char)*len);sprintf(s39," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s39;}
				| for '(' expression ';'  ';' expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s40;}
				| for '(' ';' ';' expression ')' statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s41=malloc(sizeof(char)*len);sprintf(s41," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s41;}
				| for '(' expression ';' expression ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s42;}
				| for '(' expression ';'  ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s43;}
				| for '('  ';' expression ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s44=malloc(sizeof(char)*len);sprintf(s44," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s44;}
				| for '(' ';' ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s45=malloc(sizeof(char)*len);sprintf(s45," <<<iterationStatement: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s45;}
				| for '(' var variableDeclarationList ';' expression ';' expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+strlen($<c>10)+7+28 ;char *s46=malloc(sizeof(char)*len);sprintf(s46," <<<iterationStatement: %s %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9,$<c>10);$<c>$=s46;}
				| for '(' var variableDeclarationList ';' expression ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s47=malloc(sizeof(char)*len);sprintf(s47," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s47;}
				| for '(' var variableDeclarationList ';' ';' expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s48=malloc(sizeof(char)*len);sprintf(s48," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s48;}
				| for '(' var variableDeclarationList ';'  ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s49;}
				| for '(' leftHandSideExpression in expression ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s50=malloc(sizeof(char)*len);sprintf(s50," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s50;}
				| for '(' var variableDeclaration in expression ')' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s51=malloc(sizeof(char)*len);sprintf(s51," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s51;}
				;
continueStatement	:
				 continue Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<continueStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s52;}
				| continue ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s53=malloc(sizeof(char)*len);sprintf(s53," <<<continueStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s53;}
				;
breakStatement	:
				 break Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<breakStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s54;}
				| break ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s55=malloc(sizeof(char)*len);sprintf(s55," <<<breakStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s55;}
				;
returnStatement	:
				 return expression ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s56=malloc(sizeof(char)*len);sprintf(s56," <<<returnStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s56;}
				| return ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s57=malloc(sizeof(char)*len);sprintf(s57," <<<returnStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s57;}
				;
withStatement	:
				 with '(' expression ')' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+18 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<withStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s58;}
				;
switchStatement	:
				 switch '(' expression ')' caseBlock
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s59=malloc(sizeof(char)*len);sprintf(s59," <<<switchStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s59;}
				;
caseBlock	:
				 '{' caseClauses  defaultClause caseClauses  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+14 ;char *s60=malloc(sizeof(char)*len);sprintf(s60," <<<caseBlock: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s60;}
				| '{' caseClauses defaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s61=malloc(sizeof(char)*len);sprintf(s61," <<<caseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s61;}
				| '{' caseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s62=malloc(sizeof(char)*len);sprintf(s62," <<<caseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s62;}
				| '{' defaultClause caseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s63=malloc(sizeof(char)*len);sprintf(s63," <<<caseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s63;}
				| '{' defaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s64=malloc(sizeof(char)*len);sprintf(s64," <<<caseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s64;}
				| '{' '}'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<caseBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s65;}
				;
caseClauses	:
				 caseClause 	{$<c>$=$<c>1;}
				| caseClauses caseClause
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s67=malloc(sizeof(char)*len);sprintf(s67," <<<caseClauses: %s %s >>>",$<c>1,$<c>2);$<c>$=s67;}
				;
caseClause	:
				 case expression ':' statementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+14 ;char *s68=malloc(sizeof(char)*len);sprintf(s68," <<<caseClause: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s68;}
				| case expression ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s69=malloc(sizeof(char)*len);sprintf(s69," <<<caseClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s69;}
				;
defaultClause	:
				 default ':' statementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s70=malloc(sizeof(char)*len);sprintf(s70," <<<defaultClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s70;}
				| default ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s71=malloc(sizeof(char)*len);sprintf(s71," <<<defaultClause: %s %s >>>",$<c>1,$<c>2);$<c>$=s71;}
				;
labelledStatement	:
				 Identifier ':' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s72=malloc(sizeof(char)*len);sprintf(s72," <<<labelledStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s72;}
				;
throwStatement	:
				 throw expression ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s73=malloc(sizeof(char)*len);sprintf(s73," <<<throwStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s73;}
				;
tryStatement	:
				 try block catchProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s74=malloc(sizeof(char)*len);sprintf(s74," <<<tryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s74;}
				| try block finallyProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s75=malloc(sizeof(char)*len);sprintf(s75," <<<tryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s75;}
				| try block catchProduction finallyProduction
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+16 ;char *s76=malloc(sizeof(char)*len);sprintf(s76," <<<tryStatement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s76;}
				;
catchProduction	:
				 catch '(' Identifier ')' block
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s77=malloc(sizeof(char)*len);sprintf(s77," <<<catchProduction: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s77;}
				;
finallyProduction	:
				 finally block
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s78=malloc(sizeof(char)*len);sprintf(s78," <<<finallyProduction: %s %s >>>",$<c>1,$<c>2);$<c>$=s78;}
				;
debuggerStatement	:
				 debugger ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s79=malloc(sizeof(char)*len);sprintf(s79," <<<debuggerStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s79;}
				;
functionDeclaration	:
				 function Identifier '(' formalParameterList ')' '{' functionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+27 ;char *s80=malloc(sizeof(char)*len);sprintf(s80," <<<functionDeclaration: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s80;}
				| function Identifier '('  ')' '{' functionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+26 ;char *s81=malloc(sizeof(char)*len);sprintf(s81," <<<functionDeclaration: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s81;}
				;
functionExpression	:
				 function '(' formalParameterList ')' '{' functionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s82=malloc(sizeof(char)*len);sprintf(s82," <<<functionExpression: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s82;}
				| function  '(' ')' '{' functionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s83=malloc(sizeof(char)*len);sprintf(s83," <<<functionExpression: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s83;}
				;
formalParameterList	:
				 formalParameterList ',' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s84=malloc(sizeof(char)*len);sprintf(s84," <<<formalParameterList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s84;}
				| Identifier
	{$<c>$=$<c>1;}
				;
functionBody	:
				 sourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
elementList	:
				 assignmentExpression 	{$<c>$=$<c>1;}
				|  elementList ',' assignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+14 ;char *s89=malloc(sizeof(char)*len);sprintf(s89," <<<elementList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s89;}
				;
objectLiteral	:
				 '{' propertyNameAndValueList  '}'  
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s90=malloc(sizeof(char)*len);sprintf(s90," <<<objectLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s90;}
				;
propertyNameAndValueList	:
				 propertyNameAndValueList  ',' propertyAssignment 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s91=malloc(sizeof(char)*len);sprintf(s91," <<<propertyNameAndValueList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s91;}
				| propertyAssignment
	{$<c>$=$<c>1;}
				;
propertyAssignment	:
				 propertyName ':' assignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s93=malloc(sizeof(char)*len);sprintf(s93," <<<propertyAssignment: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s93;}
				| Identifier '(' ')' '{' functionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s94=malloc(sizeof(char)*len);sprintf(s94," <<<propertyAssignment: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s94;}
				| Identifier '(' propertySetParameterList ')' '{' functionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s95=malloc(sizeof(char)*len);sprintf(s95," <<<propertyAssignment: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s95;}
				;
propertyName	:
				 StringLiteral 	{$<c>$=$<c>1;}
				| numericLiteral
	{$<c>$=$<c>1;}
				;
propertySetParameterList	:
				 Identifier
	{$<c>$=$<c>1;}
				;
arguments	:
				 '(' argumentList ')' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s99=malloc(sizeof(char)*len);sprintf(s99," <<<arguments: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s99;}
				| '(' ')'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s100=malloc(sizeof(char)*len);sprintf(s100," <<<arguments: %s %s >>>",$<c>1,$<c>2);$<c>$=s100;}
				;
argumentList	:
				 argumentList ',' assignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s101=malloc(sizeof(char)*len);sprintf(s101," <<<argumentList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s101;}
				| assignmentExpression
	{$<c>$=$<c>1;}
				;
memberExpression	:
				 primaryExpression 	{$<c>$=$<c>1;}
				| functionExpression 	{$<c>$=$<c>1;}
				| memberExpression '[' expression ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+20 ;char *s105=malloc(sizeof(char)*len);sprintf(s105," <<<memberExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s105;}
				| memberExpression '.' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s106=malloc(sizeof(char)*len);sprintf(s106," <<<memberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s106;}
				| new memberExpression Arguments 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s107=malloc(sizeof(char)*len);sprintf(s107," <<<memberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s107;}
				;
primaryExpression	:
				 this 	{$<c>$=$<c>1;}
				| identifier 	{$<c>$=$<c>1;}
				| literal 	{$<c>$=$<c>1;}
				| arrayLiteral 	{$<c>$=$<c>1;}
				| objectLiteral 	{$<c>$=$<c>1;}
				| '(' expression ')'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s113=malloc(sizeof(char)*len);sprintf(s113," <<<primaryExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s113;}
				;
arrayLiteral	:
				 '[' elision ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s114=malloc(sizeof(char)*len);sprintf(s114," <<<arrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s114;}
				| '[' elementList ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s115=malloc(sizeof(char)*len);sprintf(s115," <<<arrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s115;}
				| '[' elementList ',' elision ']'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+17 ;char *s116=malloc(sizeof(char)*len);sprintf(s116," <<<arrayLiteral: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s116;}
				;
elision	:
				 elision ',' 	{int len=strlen($<c>1)+strlen($<c>2)+7+9 ;char *s117=malloc(sizeof(char)*len);sprintf(s117," <<<elision: %s %s >>>",$<c>1,$<c>2);$<c>$=s117;}
				| 
	{$<c>$="EMPTY";}
				;
assignmentExpression	:
				 conditionalExpression 	{$<c>$=$<c>1;}
				| leftHandSideExpression '=' assignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s120=malloc(sizeof(char)*len);sprintf(s120," <<<assignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s120;}
				| leftHandSideExpression assignmentOperator assignmentExpression 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s121=malloc(sizeof(char)*len);sprintf(s121," <<<assignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s121;}
				;
leftHandSideExpression	:
				 newExpression 	{$<c>$=$<c>1;}
				| callExpression
	{$<c>$=$<c>1;}
				;
callExpression	:
				 memberExpression arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s124=malloc(sizeof(char)*len);sprintf(s124," <<<callExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s124;}
				| callExpression arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s125=malloc(sizeof(char)*len);sprintf(s125," <<<callExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s125;}
				| callExpression '[' expression ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+18 ;char *s126=malloc(sizeof(char)*len);sprintf(s126," <<<callExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s126;}
				| callExpression '.' Identifier
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s127=malloc(sizeof(char)*len);sprintf(s127," <<<callExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s127;}
				;
newExpression	:
				  memberExpression 	{$<c>$=$<c>1;}
				| new newExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s129=malloc(sizeof(char)*len);sprintf(s129," <<<newExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s129;}
				;
expression	:
				 assignmentExpression 	{$<c>$=$<c>1;}
				| expression ',' assignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s131=malloc(sizeof(char)*len);sprintf(s131," <<<expression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s131;}
				;
conditionalExpression	:
				 logicalORExpression 	{$<c>$=$<c>1;}
				| logicalORExpression '?' assignmentExpression ':' assignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+26 ;char *s133=malloc(sizeof(char)*len);sprintf(s133," <<<conditionalExpression: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s133;}
				;
logicalORExpression	:
				 logicalANDExpression 	{$<c>$=$<c>1;}
				| logicalORExpression "##" logicalANDExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s135=malloc(sizeof(char)*len);sprintf(s135," <<<logicalORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s135;}
				;
logicalANDExpression	:
				 bitwiseORExpression 	{$<c>$=$<c>1;}
				| logicalANDExpression "&&" bitwiseORExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s137=malloc(sizeof(char)*len);sprintf(s137," <<<logicalANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s137;}
				;
bitwiseORExpression	:
				 bitwiseXORExpression 	{$<c>$=$<c>1;}
				| bitwiseORExpression '#' bitwiseXORExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s139=malloc(sizeof(char)*len);sprintf(s139," <<<bitwiseORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s139;}
				;
bitwiseXORExpression	:
				 bitwiseANDExpression 	{$<c>$=$<c>1;}
				| bitwiseXORExpression '^' bitwiseANDExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s141=malloc(sizeof(char)*len);sprintf(s141," <<<bitwiseXORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s141;}
				;
bitwiseANDExpression	:
				 equalityExpression 	{$<c>$=$<c>1;}
				| bitwiseANDExpression '&' equalityExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s143=malloc(sizeof(char)*len);sprintf(s143," <<<bitwiseANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s143;}
				;
equalityExpression	:
				 relationalExpression 	{$<c>$=$<c>1;}
				| equalityExpression "==" relationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s145=malloc(sizeof(char)*len);sprintf(s145," <<<equalityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s145;}
				| equalityExpression "!=" relationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s146=malloc(sizeof(char)*len);sprintf(s146," <<<equalityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s146;}
				| equalityExpression "===" relationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s147=malloc(sizeof(char)*len);sprintf(s147," <<<equalityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s147;}
				| equalityExpression "!==" relationalExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s148=malloc(sizeof(char)*len);sprintf(s148," <<<equalityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s148;}
				;
relationalExpression	:
				 shiftExpression 	{$<c>$=$<c>1;}
				| relationalExpression '<' shiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s150=malloc(sizeof(char)*len);sprintf(s150," <<<relationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s150;}
				| relationalExpression '>' shiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s151=malloc(sizeof(char)*len);sprintf(s151," <<<relationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s151;}
				| relationalExpression "<=" shiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s152=malloc(sizeof(char)*len);sprintf(s152," <<<relationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s152;}
				| relationalExpression ">=" shiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s153=malloc(sizeof(char)*len);sprintf(s153," <<<relationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s153;}
				| relationalExpression instanceof shiftExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s154=malloc(sizeof(char)*len);sprintf(s154," <<<relationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s154;}
				;
shiftExpression	:
				 additiveExpression 	{$<c>$=$<c>1;}
				| shiftExpression "<<" additiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s156=malloc(sizeof(char)*len);sprintf(s156," <<<shiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s156;}
				| shiftExpression ">>" additiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s157=malloc(sizeof(char)*len);sprintf(s157," <<<shiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s157;}
				| shiftExpression ">>>" additiveExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s158=malloc(sizeof(char)*len);sprintf(s158," <<<shiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s158;}
				;
additiveExpression	:
				 multiplicativeExpression 	{$<c>$=$<c>1;}
				| additiveExpression '+' multiplicativeExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s160=malloc(sizeof(char)*len);sprintf(s160," <<<additiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s160;}
				| additiveExpression '-' multiplicativeExpression 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s161=malloc(sizeof(char)*len);sprintf(s161," <<<additiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s161;}
				;
multiplicativeExpression	:
				 unaryExpression 	{$<c>$=$<c>1;}
				| multiplicativeExpression '*' unaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s163=malloc(sizeof(char)*len);sprintf(s163," <<<multiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s163;}
				| multiplicativeExpression '/' unaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s164=malloc(sizeof(char)*len);sprintf(s164," <<<multiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s164;}
				| multiplicativeExpression '%' unaryExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s165=malloc(sizeof(char)*len);sprintf(s165," <<<multiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s165;}
				;
unaryExpression	:
				 delete unaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s166=malloc(sizeof(char)*len);sprintf(s166," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s166;}
				| void UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s167=malloc(sizeof(char)*len);sprintf(s167," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s167;}
				| typeof UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s168=malloc(sizeof(char)*len);sprintf(s168," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s168;}
				| "++" unaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s169=malloc(sizeof(char)*len);sprintf(s169," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s169;}
				| "--" unaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s170=malloc(sizeof(char)*len);sprintf(s170," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s170;}
				| '+' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s171=malloc(sizeof(char)*len);sprintf(s171," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s171;}
				| '-' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s172=malloc(sizeof(char)*len);sprintf(s172," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s172;}
				| '~' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s173=malloc(sizeof(char)*len);sprintf(s173," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s173;}
				| '!' UnaryExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s174=malloc(sizeof(char)*len);sprintf(s174," <<<unaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s174;}
				;
assignmentOperator	:
				 "*="  	{$<c>$=$<c>1;}
				| "/="  	{$<c>$=$<c>1;}
				| "%="  	{$<c>$=$<c>1;}
				| "+="  	{$<c>$=$<c>1;}
				| "-="  	{$<c>$=$<c>1;}
				| "<<="  	{$<c>$=$<c>1;}
				| ">>="  	{$<c>$=$<c>1;}
				| ">>>="  	{$<c>$=$<c>1;}
				| "&="  	{$<c>$=$<c>1;}
				| "^=" 
	{$<c>$=$<c>1;}
				;
literal	:
				 NullLiteral 	{$<c>$=$<c>1;}
				| BooleanLiteral 	{$<c>$=$<c>1;}
				| numericLiteral 	{$<c>$=$<c>1;}
				| StringLiteral 
	{$<c>$=$<c>1;}
				;
numericLiteral	:
				 INT_LITERAL
	{$<c>$=$<c>1;}
				;
StringLiteral	:
				 STRING_LITERAL
	{$<c>$=$<c>1;}
				;
NullLiteral	:
				 null
	{$<c>$=$<c>1;}
				;
BooleanLiteral	:
				 true 	{$<c>$=$<c>1;}
				| false
	{$<c>$=$<c>1;}
				;
Identifier	:
				 ID
	{$<c>$=$<c>1;}
				;

%%
int main()
{
yyparse();
}