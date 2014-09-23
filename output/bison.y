%token Var If Do While For In Continue Break Return With Switch Case Default Throw Try Catch Finally Debugger Function New This NewExpression Instanceof Delete Void Typeof INT_LITERAL STRING_LITERAL null true false ID ASSIGN_OP E_ASSIGN_OP CHAR_LITERAL EQ_OP COND_OP REL_OP ARITH_OP 

%left '(' '[' '*' '/' '%' '+' '-' "<<" ">>" ">>>" '<' '>' "<=" ">=" "==" "!=" '&' '^' '#' "&&" "##" '?' ':' '=' 
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
Program	:
				 SourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
SourceElements	:
				 SourceElement 	{$<c>$=$<c>1;}
				| SourceElements SourceElement
	{printf("<<<SourceElements: %s %s >>>",$<c>1,$<c>2);}
				;
SourceElement	:
				 Statement 	{$<c>$=$<c>1;}
				| FunctionDeclaration
	{$<c>$=$<c>1;}
				;
Statement	:
				 Block 	{$<c>$=$<c>1;}
				| VariableStatement 	{$<c>$=$<c>1;}
				| EmptyStatement 	{$<c>$=$<c>1;}
				| IfStatement 	{$<c>$=$<c>1;}
				| IterationStatement 	{$<c>$=$<c>1;}
				| ContinueStatement 	{$<c>$=$<c>1;}
				| BreakStatement 	{$<c>$=$<c>1;}
				| ReturnStatement 	{$<c>$=$<c>1;}
				| WithStatement 	{$<c>$=$<c>1;}
				| LabelledStatement 	{$<c>$=$<c>1;}
				| SwitchStatement 	{$<c>$=$<c>1;}
				| ThrowStatement 	{$<c>$=$<c>1;}
				| TryStatement 	{$<c>$=$<c>1;}
				| DebuggerStatement
	{$<c>$=$<c>1;}
				;
Block	:
				 '{' StatementList '}'	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s21=malloc(sizeof(char)*len);sprintf(s21," <<<Block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s21;}
				| EmptyBlock
	{$<c>$=$<c>1;}
				;
EmptyBlock	:
				 '{' '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+12 ;char *s23=malloc(sizeof(char)*len);sprintf(s23," <<<EmptyBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s23;}
				;
StatementList	:
				 Statement 	{$<c>$=$<c>1;}
				| StatementList Statement
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s25=malloc(sizeof(char)*len);sprintf(s25," <<<StatementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s25;}
				;
VariableStatement	:
				 Var VariableDeclarationList ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s26=malloc(sizeof(char)*len);sprintf(s26," <<<VariableStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s26;}
				;
VariableDeclarationList	:
				 VariableDeclarationList  ',' VariableDeclaration 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+26 ;char *s27=malloc(sizeof(char)*len);sprintf(s27," <<<VariableDeclarationList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s27;}
				| VariableDeclaration
	{$<c>$=$<c>1;}
				;
VariableDeclaration	:
				 Identifier  	{$<c>$=$<c>1;}
				| Identifier Initialiser 
	{int len=strlen($<c>1)+strlen($<c>2)+7+21 ;char *s30=malloc(sizeof(char)*len);sprintf(s30," <<<VariableDeclaration: %s %s >>>",$<c>1,$<c>2);$<c>$=s30;}
				;
Initialiser	:
				 '=' AssignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s31=malloc(sizeof(char)*len);sprintf(s31," <<<Initialiser: %s %s >>>",$<c>1,$<c>2);$<c>$=s31;}
				;
EmptyStatement	:
				 ';'
	{$<c>$=$<c>1;}
				;
IfStatement	:
				  If '(' Expression ')' Statement 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+16 ;char *s33=malloc(sizeof(char)*len);sprintf(s33," <<<IfStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s33;}
				;
IterationStatement	:
				 Do Statement While '(' Expression ')' ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s34=malloc(sizeof(char)*len);sprintf(s34," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s34;}
				| While '(' Expression ')' Statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+23 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<IterationStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s35;}
				| For '(' Expression ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s36=malloc(sizeof(char)*len);sprintf(s36," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s36;}
				| For '(' ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s37=malloc(sizeof(char)*len);sprintf(s37," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s37;}
				| For '(' Expression ';'  ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s38=malloc(sizeof(char)*len);sprintf(s38," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s38;}
				| For '(' ';' ';' Expression ')' Statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s39=malloc(sizeof(char)*len);sprintf(s39," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s39;}
				| For '(' Expression ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s40;}
				| For '(' Expression ';'  ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s41=malloc(sizeof(char)*len);sprintf(s41," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s41;}
				| For '('  ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s42;}
				| For '(' ';' ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<IterationStatement: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s43;}
				| For '(' Var VariableDeclarationList ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+strlen($<c>10)+7+28 ;char *s44=malloc(sizeof(char)*len);sprintf(s44," <<<IterationStatement: %s %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9,$<c>10);$<c>$=s44;}
				| For '(' Var VariableDeclarationList ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s45=malloc(sizeof(char)*len);sprintf(s45," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s45;}
				| For '(' Var VariableDeclarationList ';' ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s46=malloc(sizeof(char)*len);sprintf(s46," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s46;}
				| For '(' Var VariableDeclarationList ';'  ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s47=malloc(sizeof(char)*len);sprintf(s47," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s47;}
				| For '(' LeftHandSideExpression In Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s48=malloc(sizeof(char)*len);sprintf(s48," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s48;}
				| For '(' Var VariableDeclaration In Expression ')' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s49;}
				;
ContinueStatement	:
				 Continue Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s50=malloc(sizeof(char)*len);sprintf(s50," <<<ContinueStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s50;}
				| Continue ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s51=malloc(sizeof(char)*len);sprintf(s51," <<<ContinueStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s51;}
				;
BreakStatement	:
				 Break Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<BreakStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s52;}
				| Break ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s53=malloc(sizeof(char)*len);sprintf(s53," <<<BreakStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s53;}
				;
ReturnStatement	:
				 Return Expression ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<ReturnStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s54;}
				| Return ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s55=malloc(sizeof(char)*len);sprintf(s55," <<<ReturnStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s55;}
				;
WithStatement	:
				 With '(' Expression ')' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+18 ;char *s56=malloc(sizeof(char)*len);sprintf(s56," <<<WithStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s56;}
				;
SwitchStatement	:
				 Switch '(' Expression ')' CaseBlock
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s57=malloc(sizeof(char)*len);sprintf(s57," <<<SwitchStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s57;}
				;
CaseBlock	:
				 '{' CaseClauses  DefaultClause CaseClauses  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+14 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<CaseBlock: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s58;}
				| '{' CaseClauses DefaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s59=malloc(sizeof(char)*len);sprintf(s59," <<<CaseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s59;}
				| '{' CaseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s60=malloc(sizeof(char)*len);sprintf(s60," <<<CaseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s60;}
				| '{' DefaultClause CaseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s61=malloc(sizeof(char)*len);sprintf(s61," <<<CaseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s61;}
				| '{' DefaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s62=malloc(sizeof(char)*len);sprintf(s62," <<<CaseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s62;}
				| '{' '}'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s63=malloc(sizeof(char)*len);sprintf(s63," <<<CaseBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s63;}
				;
CaseClauses	:
				 CaseClause 	{$<c>$=$<c>1;}
				| CaseClauses CaseClause
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<CaseClauses: %s %s >>>",$<c>1,$<c>2);$<c>$=s65;}
				;
CaseClause	:
				 Case Expression ':' StatementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+14 ;char *s66=malloc(sizeof(char)*len);sprintf(s66," <<<CaseClause: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s66;}
				| Case Expression ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s67=malloc(sizeof(char)*len);sprintf(s67," <<<CaseClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s67;}
				;
DefaultClause	:
				 Default ':' StatementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s68=malloc(sizeof(char)*len);sprintf(s68," <<<DefaultClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s68;}
				| Default ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s69=malloc(sizeof(char)*len);sprintf(s69," <<<DefaultClause: %s %s >>>",$<c>1,$<c>2);$<c>$=s69;}
				;
LabelledStatement	:
				 Identifier ':' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s70=malloc(sizeof(char)*len);sprintf(s70," <<<LabelledStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s70;}
				;
ThrowStatement	:
				 Throw Expression ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s71=malloc(sizeof(char)*len);sprintf(s71," <<<ThrowStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s71;}
				;
TryStatement	:
				 Try Block CatchProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s72=malloc(sizeof(char)*len);sprintf(s72," <<<TryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s72;}
				| Try Block FinallyProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s73=malloc(sizeof(char)*len);sprintf(s73," <<<TryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s73;}
				| Try Block CatchProduction FinallyProduction
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+16 ;char *s74=malloc(sizeof(char)*len);sprintf(s74," <<<TryStatement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s74;}
				;
CatchProduction	:
				 Catch '(' Identifier ')' Block
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s75=malloc(sizeof(char)*len);sprintf(s75," <<<CatchProduction: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s75;}
				;
FinallyProduction	:
				 Finally Block
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s76=malloc(sizeof(char)*len);sprintf(s76," <<<FinallyProduction: %s %s >>>",$<c>1,$<c>2);$<c>$=s76;}
				;
DebuggerStatement	:
				 Debugger ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s77=malloc(sizeof(char)*len);sprintf(s77," <<<DebuggerStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s77;}
				;
FunctionDeclaration	:
				 Function Identifier '(' FormalParameterList ')' '{' FunctionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+27 ;char *s78=malloc(sizeof(char)*len);sprintf(s78," <<<FunctionDeclaration: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s78;}
				| Function Identifier '('  ')' '{' FunctionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+26 ;char *s79=malloc(sizeof(char)*len);sprintf(s79," <<<FunctionDeclaration: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s79;}
				;
FunctionExpression	:
				 Function '(' FormalParameterList ')' '{' FunctionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s80=malloc(sizeof(char)*len);sprintf(s80," <<<FunctionExpression: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s80;}
				| Function  '(' ')' '{' FunctionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s81=malloc(sizeof(char)*len);sprintf(s81," <<<FunctionExpression: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s81;}
				;
FormalParameterList	:
				 FormalParameterList ',' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s82=malloc(sizeof(char)*len);sprintf(s82," <<<FormalParameterList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s82;}
				| Identifier
	{$<c>$=$<c>1;}
				;
FunctionBody	:
				 SourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;
ElementList	:
				 AssignmentExpression 	{$<c>$=$<c>1;}
				|  ElementList ',' AssignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+14 ;char *s87=malloc(sizeof(char)*len);sprintf(s87," <<<ElementList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s87;}
				;
ObjectLiteral	:
				 '{' PropertyNameAndValueList  '}'  
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s88=malloc(sizeof(char)*len);sprintf(s88," <<<ObjectLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s88;}
				;
PropertyNameAndValueList	:
				 PropertyNameAndValueList  ',' PropertyAssignment 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s89=malloc(sizeof(char)*len);sprintf(s89," <<<PropertyNameAndValueList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s89;}
				| PropertyAssignment
	{$<c>$=$<c>1;}
				;
PropertyAssignment	:
				 Identifier ':' Expression 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s91=malloc(sizeof(char)*len);sprintf(s91," <<<PropertyAssignment: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s91;}
				;
Arguments	:
				 '(' ArgumentList ')' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s92=malloc(sizeof(char)*len);sprintf(s92," <<<Arguments: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s92;}
				| '(' ')'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s93=malloc(sizeof(char)*len);sprintf(s93," <<<Arguments: %s %s >>>",$<c>1,$<c>2);$<c>$=s93;}
				;
ArgumentList	:
				 ArgumentList ',' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s94=malloc(sizeof(char)*len);sprintf(s94," <<<ArgumentList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s94;}
				| AssignmentExpression
	{$<c>$=$<c>1;}
				;
MemberExpression	:
				 PrimaryExpression 	{$<c>$=$<c>1;}
				| FunctionExpression 	{$<c>$=$<c>1;}
				| MemberExpression '[' Expression ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+20 ;char *s98=malloc(sizeof(char)*len);sprintf(s98," <<<MemberExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s98;}
				| MemberExpression '.' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s99=malloc(sizeof(char)*len);sprintf(s99," <<<MemberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s99;}
				| New MemberExpression Arguments 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s100=malloc(sizeof(char)*len);sprintf(s100," <<<MemberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s100;}
				;
PrimaryExpression	:
				 This 	{$<c>$=$<c>1;}
				| NullLiteral 	{$<c>$=$<c>1;}
				| BooleanLiteral 	{$<c>$=$<c>1;}
				| ArrayLiteral 	{$<c>$=$<c>1;}
				| ObjectLiteral 	{$<c>$=$<c>1;}
				| '(' Expression ')' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s106=malloc(sizeof(char)*len);sprintf(s106," <<<PrimaryExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s106;}
				| NumericLiteral 	{$<c>$=$<c>1;}
				| StringLiteral
	{$<c>$=$<c>1;}
				;
ArrayLiteral	:
				 '[' Elision ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s109=malloc(sizeof(char)*len);sprintf(s109," <<<ArrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s109;}
				| '[' ElementList ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s110=malloc(sizeof(char)*len);sprintf(s110," <<<ArrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s110;}
				| '[' ElementList ',' Elision ']'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+17 ;char *s111=malloc(sizeof(char)*len);sprintf(s111," <<<ArrayLiteral: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s111;}
				;
Elision	:
				 Elision ',' 	{int len=strlen($<c>1)+strlen($<c>2)+7+9 ;char *s112=malloc(sizeof(char)*len);sprintf(s112," <<<Elision: %s %s >>>",$<c>1,$<c>2);$<c>$=s112;}
				| 
	{$<c>$="EMPTY";}
				;
AssignmentExpression	:
				 ConditionalExpression 	{$<c>$=$<c>1;}
				| LeftHandSideExpression '=' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s115=malloc(sizeof(char)*len);sprintf(s115," <<<AssignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s115;}
				| LeftHandSideExpression AssignmentOperator AssignmentExpression 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s116=malloc(sizeof(char)*len);sprintf(s116," <<<AssignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s116;}
				;
LeftHandSideExpression	:
				 New NewExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+24 ;char *s117=malloc(sizeof(char)*len);sprintf(s117," <<<LeftHandSideExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s117;}
				| CallExpression 
	{$<c>$=$<c>1;}
				;
CallExpression	:
				 MemberExpression Arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s119=malloc(sizeof(char)*len);sprintf(s119," <<<CallExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s119;}
				| CallExpression '.' Identifier
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s120=malloc(sizeof(char)*len);sprintf(s120," <<<CallExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s120;}
				;
Expression	:
				 AssignmentExpression 
	{$<c>$=$<c>1;}
				;
ConditionalExpression	:
				 LogicalORExpression '?' AssignmentExpression ':' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+26 ;char *s122=malloc(sizeof(char)*len);sprintf(s122," <<<ConditionalExpression: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s122;}
				| LogicalORExpression
	{$<c>$=$<c>1;}
				;
LogicalORExpression	:
				 LogicalORExpression "##" LogicalANDExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s124=malloc(sizeof(char)*len);sprintf(s124," <<<LogicalORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s124;}
				| LogicalANDExpression
	{$<c>$=$<c>1;}
				;
LogicalANDExpression	:
				 LogicalANDExpression "&&" BitwiseORExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s126=malloc(sizeof(char)*len);sprintf(s126," <<<LogicalANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s126;}
				| BitwiseORExpression
	{$<c>$=$<c>1;}
				;
BitwiseORExpression	:
				  BitwiseORExpression '#' BitwiseXORExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s128=malloc(sizeof(char)*len);sprintf(s128," <<<BitwiseORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s128;}
				| BitwiseXORExpression
	{$<c>$=$<c>1;}
				;
BitwiseXORExpression	:
				 BitwiseXORExpression '^' BitwiseANDExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s130=malloc(sizeof(char)*len);sprintf(s130," <<<BitwiseXORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s130;}
				| BitwiseANDExpression
	{$<c>$=$<c>1;}
				;
BitwiseANDExpression	:
				 BitwiseANDExpression '&' EqualityExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s132=malloc(sizeof(char)*len);sprintf(s132," <<<BitwiseANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s132;}
				| EqualityExpression
	{$<c>$=$<c>1;}
				;
EqualityExpression	:
				 EqualityExpression "==" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s134=malloc(sizeof(char)*len);sprintf(s134," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s134;}
				| EqualityExpression "!=" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s135=malloc(sizeof(char)*len);sprintf(s135," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s135;}
				| EqualityExpression "===" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s136=malloc(sizeof(char)*len);sprintf(s136," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s136;}
				| EqualityExpression "!==" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s137=malloc(sizeof(char)*len);sprintf(s137," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s137;}
				| RelationalExpression
	{$<c>$=$<c>1;}
				;
RelationalExpression	:
				 RelationalExpression '<' ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s139=malloc(sizeof(char)*len);sprintf(s139," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s139;}
				| RelationalExpression '>' ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s140=malloc(sizeof(char)*len);sprintf(s140," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s140;}
				| RelationalExpression "<=" ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s141=malloc(sizeof(char)*len);sprintf(s141," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s141;}
				| RelationalExpression ">=" ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s142=malloc(sizeof(char)*len);sprintf(s142," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s142;}
				| RelationalExpression Instanceof ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s143=malloc(sizeof(char)*len);sprintf(s143," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s143;}
				| ShiftExpression   
	{$<c>$=$<c>1;}
				;
ShiftExpression	:
				 ShiftExpression "<<" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s145=malloc(sizeof(char)*len);sprintf(s145," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s145;}
				| ShiftExpression ">>" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s146=malloc(sizeof(char)*len);sprintf(s146," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s146;}
				| ShiftExpression ">>>" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s147=malloc(sizeof(char)*len);sprintf(s147," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s147;}
				| AdditiveExpression
	{$<c>$=$<c>1;}
				;
AdditiveExpression	:
				 AdditiveExpression '+' MultiplicativeExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s149=malloc(sizeof(char)*len);sprintf(s149," <<<AdditiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s149;}
				| AdditiveExpression '-' MultiplicativeExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s150=malloc(sizeof(char)*len);sprintf(s150," <<<AdditiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s150;}
				| MultiplicativeExpression
	{$<c>$=$<c>1;}
				;
MultiplicativeExpression	:
				 MultiplicativeExpression '*' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s152=malloc(sizeof(char)*len);sprintf(s152," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s152;}
				| MultiplicativeExpression '/' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s153=malloc(sizeof(char)*len);sprintf(s153," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s153;}
				| MultiplicativeExpression '%' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s154=malloc(sizeof(char)*len);sprintf(s154," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s154;}
				| UnaryExpression
	{$<c>$=$<c>1;}
				;
UnaryExpression	:
				 Delete UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s156=malloc(sizeof(char)*len);sprintf(s156," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s156;}
				| Void UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s157=malloc(sizeof(char)*len);sprintf(s157," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s157;}
				| Typeof UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s158=malloc(sizeof(char)*len);sprintf(s158," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s158;}
				| "++" UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s159=malloc(sizeof(char)*len);sprintf(s159," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s159;}
				| "--" UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s160=malloc(sizeof(char)*len);sprintf(s160," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s160;}
				| '+' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s161=malloc(sizeof(char)*len);sprintf(s161," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s161;}
				| '-' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s162=malloc(sizeof(char)*len);sprintf(s162," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s162;}
				| '~' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s163=malloc(sizeof(char)*len);sprintf(s163," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s163;}
				| '!' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s164=malloc(sizeof(char)*len);sprintf(s164," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s164;}
				| LeftHandSideExpression
	{$<c>$=$<c>1;}
				;
AssignmentOperator	:
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
NumericLiteral	:
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