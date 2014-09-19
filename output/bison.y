%token INT_LITERAL STRING_LITERAL null true false Class Enum Extends Super Const Export Import Implements Let Private Public Interface Package Protected Static Yield SemiColon break do instanceof typeof case else new var catch finally return void continue for switch while debugger function this with default if throw delete in try ID ASSIGN_OP E_ASSIGN_OP CHAR_LITERAL EQ_OP COND_OP REL_OP ARITH_OP 
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
				| sourceElement sourceElements
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
				| expressionStatement 	{$<c>$=$<c>1;}
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
				 '{' statementList '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s22=malloc(sizeof(char)*len);sprintf(s22," <<<block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s22;}
				;
statementList	:
				 statement 	{$<c>$=$<c>1;}
				| statement statementList 	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s24=malloc(sizeof(char)*len);sprintf(s24," <<<statementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s24;}
				| 
	{$<c>$="EMPTY";}
				;
variableStatement	:
				 Var variableDeclarationList eos
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s26=malloc(sizeof(char)*len);sprintf(s26," <<<variableStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s26;}
				;
variableDeclarationList	:
				 variableDeclaration ',' variableDeclarationList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+26 ;char *s27=malloc(sizeof(char)*len);sprintf(s27," <<<variableDeclarationList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s27;}
				| variableDeclaration
	{$<c>$=$<c>1;}
				;
variableDeclaration	:
				 Identifier  	{$<c>$=$<c>1;}
				| Identifier initialiser 	{int len=strlen($<c>1)+strlen($<c>2)+7+21 ;char *s30=malloc(sizeof(char)*len);sprintf(s30," <<<variableDeclaration: %s %s >>>",$<c>1,$<c>2);$<c>$=s30;}
				| 
	{$<c>$="EMPTY";}
				;
initialiser	:
				 '=' singleExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s32=malloc(sizeof(char)*len);sprintf(s32," <<<initialiser: %s %s >>>",$<c>1,$<c>2);$<c>$=s32;}
				;
emptyStatement	:
				 ';'
	{$<c>$=$<c>1;}
				;
expressionStatement	:
				 expressionSequence
	{$<c>$=$<c>1;}
				;
ifStatement	:
				 If '(' expressionSequence ')' statement Else statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+18 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<ifStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s35;}
				| If '(' expressionSequence ')' statement 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+16 ;char *s36=malloc(sizeof(char)*len);sprintf(s36," <<<ifStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s36;}
				;
iterationStatement	:
				 Do statement While '(' expressionSequence ')' eos 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s37=malloc(sizeof(char)*len);sprintf(s37," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s37;}
				| While '(' expressionSequence ')' statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+23 ;char *s38=malloc(sizeof(char)*len);sprintf(s38," <<<iterationStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s38;}
				| For '(' expressionSequence ';' expressionSequence ';' expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s39=malloc(sizeof(char)*len);sprintf(s39," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s39;}
				| For '(' ';' expressionSequence ';' expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s40;}
				| For '(' expressionSequence ';'  ';' expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s41=malloc(sizeof(char)*len);sprintf(s41," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s41;}
				| For '(' ';' ';' expressionSequence ')' statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s42;}
				| For '(' expressionSequence ';' expressionSequence ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s43;}
				| For '(' expressionSequence ';'  ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s44=malloc(sizeof(char)*len);sprintf(s44," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s44;}
				| For '('  ';' expressionSequence ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s45=malloc(sizeof(char)*len);sprintf(s45," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s45;}
				| For '(' ';' ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s46=malloc(sizeof(char)*len);sprintf(s46," <<<iterationStatement: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s46;}
				| For '(' Var variableDeclarationList ';' expressionSequence ';' expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+strlen($<c>10)+7+28 ;char *s47=malloc(sizeof(char)*len);sprintf(s47," <<<iterationStatement: %s %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9,$<c>10);$<c>$=s47;}
				| For '(' Var variableDeclarationList ';' expressionSequence ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s48=malloc(sizeof(char)*len);sprintf(s48," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s48;}
				| For '(' Var variableDeclarationList ';' ';' expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s49;}
				| For '(' Var variableDeclarationList ';'  ';'  ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s50=malloc(sizeof(char)*len);sprintf(s50," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s50;}
				| For '(' singleExpression In expressionSequence ')' statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s51=malloc(sizeof(char)*len);sprintf(s51," <<<iterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s51;}
				| For '(' Var variableDeclaration In expressionSequence ')' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s52;}
				;
continueStatement	:
				 Continue Identifier eos 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s53=malloc(sizeof(char)*len);sprintf(s53," <<<continueStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s53;}
				| Continue eos
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<continueStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s54;}
				;
breakStatement	:
				 Break Identifier eos 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s55=malloc(sizeof(char)*len);sprintf(s55," <<<breakStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s55;}
				| Break eos
	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s56=malloc(sizeof(char)*len);sprintf(s56," <<<breakStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s56;}
				;
returnStatement	:
				 Return expressionSequence eos 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s57=malloc(sizeof(char)*len);sprintf(s57," <<<returnStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s57;}
				| Return eos
	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<returnStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s58;}
				;
withStatement	:
				 With '(' expressionSequence ')' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+18 ;char *s59=malloc(sizeof(char)*len);sprintf(s59," <<<withStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s59;}
				;
switchStatement	:
				 Switch '(' expressionSequence ')' caseBlock
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s60=malloc(sizeof(char)*len);sprintf(s60," <<<switchStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s60;}
				;
caseBlock	:
				 '{' caseClauses  defaultClause caseClauses  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+14 ;char *s61=malloc(sizeof(char)*len);sprintf(s61," <<<caseBlock: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s61;}
				| '{' caseClauses defaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s62=malloc(sizeof(char)*len);sprintf(s62," <<<caseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s62;}
				| '{' caseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s63=malloc(sizeof(char)*len);sprintf(s63," <<<caseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s63;}
				| '{' defaultClause caseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s64=malloc(sizeof(char)*len);sprintf(s64," <<<caseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s64;}
				| '{' defaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<caseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s65;}
				| '{' '}'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s66=malloc(sizeof(char)*len);sprintf(s66," <<<caseBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s66;}
				;
caseClauses	:
				 caseClause 	{$<c>$=$<c>1;}
				| caseClause caseClauses
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s68=malloc(sizeof(char)*len);sprintf(s68," <<<caseClauses: %s %s >>>",$<c>1,$<c>2);$<c>$=s68;}
				;
caseClause	:
				 Case expressionSequence ':' statementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+14 ;char *s69=malloc(sizeof(char)*len);sprintf(s69," <<<caseClause: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s69;}
				| Case expressionSequence ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s70=malloc(sizeof(char)*len);sprintf(s70," <<<caseClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s70;}
				;
defaultClause	:
				 Default ':' statementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s71=malloc(sizeof(char)*len);sprintf(s71," <<<defaultClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s71;}
				| Default ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s72=malloc(sizeof(char)*len);sprintf(s72," <<<defaultClause: %s %s >>>",$<c>1,$<c>2);$<c>$=s72;}
				;
labelledStatement	:
				 Identifier ':' statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s73=malloc(sizeof(char)*len);sprintf(s73," <<<labelledStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s73;}
				;
throwStatement	:
				 Throw expressionSequence eos
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s74=malloc(sizeof(char)*len);sprintf(s74," <<<throwStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s74;}
				;
tryStatement	:
				 Try block catchProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s75=malloc(sizeof(char)*len);sprintf(s75," <<<tryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s75;}
				| Try block finallyProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s76=malloc(sizeof(char)*len);sprintf(s76," <<<tryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s76;}
				| Try block catchProduction finallyProduction
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+16 ;char *s77=malloc(sizeof(char)*len);sprintf(s77," <<<tryStatement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s77;}
				;
catchProduction	:
				 Catch '(' Identifier ')' block
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s78=malloc(sizeof(char)*len);sprintf(s78," <<<catchProduction: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s78;}
				;
finallyProduction	:
				 Finally block
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s79=malloc(sizeof(char)*len);sprintf(s79," <<<finallyProduction: %s %s >>>",$<c>1,$<c>2);$<c>$=s79;}
				;
debuggerStatement	:
				 Debugger eos
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s80=malloc(sizeof(char)*len);sprintf(s80," <<<debuggerStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s80;}
				;
functionDeclaration	:
				 Function Identifier '(' formalParameterList ')' '{' functionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+27 ;char *s81=malloc(sizeof(char)*len);sprintf(s81," <<<functionDeclaration: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s81;}
				| Function Identifier '('  ')' '{' functionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+26 ;char *s82=malloc(sizeof(char)*len);sprintf(s82," <<<functionDeclaration: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s82;}
				;
formalParameterList	:
				 Identifier ',' formalParameterList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s83=malloc(sizeof(char)*len);sprintf(s83," <<<formalParameterList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s83;}
				| Identifier
	{$<c>$=$<c>1;}
				;
functionBody	:
				 sourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
arrayLiteral	:
				 '[' ']' 	{int len=strlen($<c>1)+strlen($<c>2)+7+14 ;char *s87=malloc(sizeof(char)*len);sprintf(s87," <<<arrayLiteral: %s %s >>>",$<c>1,$<c>2);$<c>$=s87;}
				| '[' elementList  ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s88=malloc(sizeof(char)*len);sprintf(s88," <<<arrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s88;}
				| '[' elementList ',' elision ']'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+17 ;char *s89=malloc(sizeof(char)*len);sprintf(s89," <<<arrayLiteral: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s89;}
				;
elementList	:
				  elisionExpr elementList 	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s90=malloc(sizeof(char)*len);sprintf(s90," <<<elementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s90;}
				| elisionExpr
	{$<c>$=$<c>1;}
				;
elisionExprs	:
				 elisionExpr ',' elisionExprs 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s92=malloc(sizeof(char)*len);sprintf(s92," <<<elisionExprs: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s92;}
				| elisionExpr 
	{$<c>$=$<c>1;}
				;
elisionExpr	:
				 elision singleExpression  
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s94=malloc(sizeof(char)*len);sprintf(s94," <<<elisionExpr: %s %s >>>",$<c>1,$<c>2);$<c>$=s94;}
				;
elision	:
				 ',' 	{$<c>$=$<c>1;}
				| elision ',' 	{int len=strlen($<c>1)+strlen($<c>2)+7+9 ;char *s96=malloc(sizeof(char)*len);sprintf(s96," <<<elision: %s %s >>>",$<c>1,$<c>2);$<c>$=s96;}
				| 
	{$<c>$="EMPTY";}
				;
objectLiteral	:
				 '{' propertyNameAndValueList ',' '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+17 ;char *s98=malloc(sizeof(char)*len);sprintf(s98," <<<objectLiteral: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s98;}
				| '{' propertyNameAndValueList  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s99=malloc(sizeof(char)*len);sprintf(s99," <<<objectLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s99;}
				| '{'  ',' '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s100=malloc(sizeof(char)*len);sprintf(s100," <<<objectLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s100;}
				| '{'   '}'
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s101=malloc(sizeof(char)*len);sprintf(s101," <<<objectLiteral: %s %s >>>",$<c>1,$<c>2);$<c>$=s101;}
				;
propertyNameAndValueList	:
				 propertyAssignments propertyNameAndValueList 	{int len=strlen($<c>1)+strlen($<c>2)+7+26 ;char *s102=malloc(sizeof(char)*len);sprintf(s102," <<<propertyNameAndValueList: %s %s >>>",$<c>1,$<c>2);$<c>$=s102;}
				| propertyAssignment
	{$<c>$=$<c>1;}
				;
propertyAssignments	:
				 propertyAssignment ',' propertyAssignments 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s104=malloc(sizeof(char)*len);sprintf(s104," <<<propertyAssignments: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s104;}
				;
propertyAssignment	:
				 propertyName ':' singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s105=malloc(sizeof(char)*len);sprintf(s105," <<<propertyAssignment: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s105;}
				| Identifier '(' ')' '{' functionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s106=malloc(sizeof(char)*len);sprintf(s106," <<<propertyAssignment: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s106;}
				| Identifier '(' propertySetParameterList ')' '{' functionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s107=malloc(sizeof(char)*len);sprintf(s107," <<<propertyAssignment: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s107;}
				;
propertyName	:
				 identifierName 	{$<c>$=$<c>1;}
				| StringLiteral 	{$<c>$=$<c>1;}
				| numericLiteral
	{$<c>$=$<c>1;}
				;
propertySetParameterList	:
				 Identifier
	{$<c>$=$<c>1;}
				;
arguments	:
				 '(' argumentList ')' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s112=malloc(sizeof(char)*len);sprintf(s112," <<<arguments: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s112;}
				| '(' ')'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s113=malloc(sizeof(char)*len);sprintf(s113," <<<arguments: %s %s >>>",$<c>1,$<c>2);$<c>$=s113;}
				;
argumentList	:
				 singleExpressions argumentList 	{int len=strlen($<c>1)+strlen($<c>2)+7+14 ;char *s114=malloc(sizeof(char)*len);sprintf(s114," <<<argumentList: %s %s >>>",$<c>1,$<c>2);$<c>$=s114;}
				| singleExpression
	{$<c>$=$<c>1;}
				;
singleExpressions	:
				 singleExpression ',' singleExpressions
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s116=malloc(sizeof(char)*len);sprintf(s116," <<<singleExpressions: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s116;}
				;
expressionSequence	:
				 singleExpressions expressionSequence 	{int len=strlen($<c>1)+strlen($<c>2)+7+20 ;char *s117=malloc(sizeof(char)*len);sprintf(s117," <<<expressionSequence: %s %s >>>",$<c>1,$<c>2);$<c>$=s117;}
				| singleExpression
	{$<c>$=$<c>1;}
				;
singleExpression	:
				 singleExpression '[' expressionSequence ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+20 ;char *s119=malloc(sizeof(char)*len);sprintf(s119," <<<singleExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s119;}
				| singleExpression '.' identifierName 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s120=malloc(sizeof(char)*len);sprintf(s120," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s120;}
				| singleExpression arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s121=malloc(sizeof(char)*len);sprintf(s121," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s121;}
				| New singleExpression arguments 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s122=malloc(sizeof(char)*len);sprintf(s122," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s122;}
				| New singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s123=malloc(sizeof(char)*len);sprintf(s123," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s123;}
				| singleExpression "++" 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s124=malloc(sizeof(char)*len);sprintf(s124," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s124;}
				| singleExpression  "--" 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s125=malloc(sizeof(char)*len);sprintf(s125," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s125;}
				| Delete singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s126=malloc(sizeof(char)*len);sprintf(s126," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s126;}
				| Void singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s127=malloc(sizeof(char)*len);sprintf(s127," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s127;}
				| Typeof singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s128=malloc(sizeof(char)*len);sprintf(s128," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s128;}
				| "++" literal 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s129=malloc(sizeof(char)*len);sprintf(s129," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s129;}
				| "--" literal 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s130=malloc(sizeof(char)*len);sprintf(s130," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s130;}
				| '+' literal 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s131=malloc(sizeof(char)*len);sprintf(s131," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s131;}
				| '-' literal 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s132=malloc(sizeof(char)*len);sprintf(s132," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s132;}
				| '~' singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s133=malloc(sizeof(char)*len);sprintf(s133," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s133;}
				| '!' singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+18 ;char *s134=malloc(sizeof(char)*len);sprintf(s134," <<<singleExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s134;}
				| literal '*' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s135=malloc(sizeof(char)*len);sprintf(s135," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s135;}
				| literal '/' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s136=malloc(sizeof(char)*len);sprintf(s136," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s136;}
				| literal '%' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s137=malloc(sizeof(char)*len);sprintf(s137," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s137;}
				| literal '+' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s138=malloc(sizeof(char)*len);sprintf(s138," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s138;}
				| literal '-' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s139=malloc(sizeof(char)*len);sprintf(s139," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s139;}
				| literal "<<" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s140=malloc(sizeof(char)*len);sprintf(s140," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s140;}
				| literal ">>" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s141=malloc(sizeof(char)*len);sprintf(s141," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s141;}
				| literal ">>>" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s142=malloc(sizeof(char)*len);sprintf(s142," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s142;}
				| literal '<' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s143=malloc(sizeof(char)*len);sprintf(s143," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s143;}
				| literal '>' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s144=malloc(sizeof(char)*len);sprintf(s144," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s144;}
				| literal "<=" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s145=malloc(sizeof(char)*len);sprintf(s145," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s145;}
				| literal ">=" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s146=malloc(sizeof(char)*len);sprintf(s146," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s146;}
				| singleExpression Instanceof singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s147=malloc(sizeof(char)*len);sprintf(s147," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s147;}
				| singleExpression In singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s148=malloc(sizeof(char)*len);sprintf(s148," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s148;}
				| literal "==" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s149=malloc(sizeof(char)*len);sprintf(s149," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s149;}
				| literal "!=" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s150=malloc(sizeof(char)*len);sprintf(s150," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s150;}
				| literal "===" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s151=malloc(sizeof(char)*len);sprintf(s151," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s151;}
				| literal "!==" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s152=malloc(sizeof(char)*len);sprintf(s152," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s152;}
				| literal '&' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s153=malloc(sizeof(char)*len);sprintf(s153," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s153;}
				| literal '^' literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s154=malloc(sizeof(char)*len);sprintf(s154," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s154;}
				|  literal "&&" literal 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s155=malloc(sizeof(char)*len);sprintf(s155," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s155;}
				| singleExpression '?' singleExpression ':' singleExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+21 ;char *s156=malloc(sizeof(char)*len);sprintf(s156," <<<singleExpression: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s156;}
				| singleExpression '=' expressionSequence 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s157=malloc(sizeof(char)*len);sprintf(s157," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s157;}
				| singleExpression assignmentOperator expressionSequence 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s158=malloc(sizeof(char)*len);sprintf(s158," <<<singleExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s158;}
				| This 	{$<c>$=$<c>1;}
				| Identifier 	{$<c>$=$<c>1;}
				| literal 	{$<c>$=$<c>1;}
				| arrayLiteral 	{$<c>$=$<c>1;}
				| objectLiteral                                                          
	{$<c>$=$<c>1;}
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
identifierName	:
				 Identifier 	{$<c>$=$<c>1;}
				| reservedWord
	{$<c>$=$<c>1;}
				;
keyword	:
				 Break 	{$<c>$=$<c>1;}
				| Do 	{$<c>$=$<c>1;}
				| Instanceof 	{$<c>$=$<c>1;}
				| Typeof 	{$<c>$=$<c>1;}
				| Case 	{$<c>$=$<c>1;}
				| Else 	{$<c>$=$<c>1;}
				| New 	{$<c>$=$<c>1;}
				| Var 	{$<c>$=$<c>1;}
				| Catch 	{$<c>$=$<c>1;}
				| Finally 	{$<c>$=$<c>1;}
				| Return 	{$<c>$=$<c>1;}
				| Void 	{$<c>$=$<c>1;}
				| Continue 	{$<c>$=$<c>1;}
				| For 	{$<c>$=$<c>1;}
				| Switch 	{$<c>$=$<c>1;}
				| While 	{$<c>$=$<c>1;}
				| Debugger 	{$<c>$=$<c>1;}
				| Function 	{$<c>$=$<c>1;}
				| This 	{$<c>$=$<c>1;}
				| With 	{$<c>$=$<c>1;}
				| Default 	{$<c>$=$<c>1;}
				| If 	{$<c>$=$<c>1;}
				| Throw 	{$<c>$=$<c>1;}
				| Delete 	{$<c>$=$<c>1;}
				| In 	{$<c>$=$<c>1;}
				| Try
	{$<c>$=$<c>1;}
				;
reservedWord	:
				 keyword 	{$<c>$=$<c>1;}
				| futureReservedWord 	{$<c>$=$<c>1;}
				| NullLiteral 	{$<c>$=$<c>1;}
				| BooleanLiteral
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
futureReservedWord	:
				 Class 	{$<c>$=$<c>1;}
				| Enum 	{$<c>$=$<c>1;}
				| Extends 	{$<c>$=$<c>1;}
				| Super 	{$<c>$=$<c>1;}
				| Const 	{$<c>$=$<c>1;}
				| Export 	{$<c>$=$<c>1;}
				| Import 	{$<c>$=$<c>1;}
				| Implements 	{$<c>$=$<c>1;}
				| Let 	{$<c>$=$<c>1;}
				| Private 	{$<c>$=$<c>1;}
				| Public 	{$<c>$=$<c>1;}
				| Interface 	{$<c>$=$<c>1;}
				| Package 	{$<c>$=$<c>1;}
				| Protected 	{$<c>$=$<c>1;}
				| Static 	{$<c>$=$<c>1;}
				| Yield
	{$<c>$=$<c>1;}
				;
eos	:
				 SemiColon 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
Break	:
				 break
	{$<c>$=$<c>1;}
				;
Do	:
				 do 
	{$<c>$=$<c>1;}
				;
Instanceof	:
				 instanceof 
	{$<c>$=$<c>1;}
				;
Typeof	:
				 typeof 
	{$<c>$=$<c>1;}
				;
Case	:
				 case 
	{$<c>$=$<c>1;}
				;
Else	:
				 else 
	{$<c>$=$<c>1;}
				;
New	:
				 new 
	{$<c>$=$<c>1;}
				;
Var	:
				 var 
	{$<c>$=$<c>1;}
				;
Catch	:
				 catch 
	{$<c>$=$<c>1;}
				;
Finally	:
				 finally 
	{$<c>$=$<c>1;}
				;
Return	:
				 return 
	{$<c>$=$<c>1;}
				;
Void	:
				 void 
	{$<c>$=$<c>1;}
				;
Continue	:
				 continue 
	{$<c>$=$<c>1;}
				;
For	:
				 for 
	{$<c>$=$<c>1;}
				;
Switch	:
				 switch 
	{$<c>$=$<c>1;}
				;
While	:
				 while 
	{$<c>$=$<c>1;}
				;
Debugger	:
				 debugger 
	{$<c>$=$<c>1;}
				;
Function	:
				 function 
	{$<c>$=$<c>1;}
				;
This	:
				 this 
	{$<c>$=$<c>1;}
				;
With	:
				 with 
	{$<c>$=$<c>1;}
				;
Default	:
				 default 
	{$<c>$=$<c>1;}
				;
If	:
				 if 
	{$<c>$=$<c>1;}
				;
Throw	:
				 throw 
	{$<c>$=$<c>1;}
				;
Delete	:
				 delete 
	{$<c>$=$<c>1;}
				;
In	:
				 in 
	{$<c>$=$<c>1;}
				;
Try	:
				 try 
	{$<c>$=$<c>1;}
				;
Identifier	:
				 ID	{$<c>$=$<c>1;}
				;

%%
int main()
{
yyparse();
}