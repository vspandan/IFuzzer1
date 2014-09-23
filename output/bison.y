%token this Identifier Literal NumericLiteral StringLiteral new delete void typeof instanceof in var if else do while for continue break return with switch case default throw try catch finally block debugger function ASSIGN_OP INT_LITERAL STRING_LITERAL ID E_ASSIGN_OP CHAR_LITERAL EQ_OP COND_OP REL_OP ARITH_OP 

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
PrimaryExpression	:
				 this 	{$<c>$=$<c>1;}
				| Identifier 	{$<c>$=$<c>1;}
				| Literal 	{$<c>$=$<c>1;}
				| ArrayLiteral 	{$<c>$=$<c>1;}
				| ObjectLiteral 	{$<c>$=$<c>1;}
				| '(' Expression ')'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s12=malloc(sizeof(char)*len);sprintf(s12," <<<PrimaryExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s12;}
				;
ArrayLiteral	:
				 '[' Elision ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s13=malloc(sizeof(char)*len);sprintf(s13," <<<ArrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s13;}
				| '[' ElementList ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s14=malloc(sizeof(char)*len);sprintf(s14," <<<ArrayLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s14;}
				| '[' ElementList ',' Elision ']'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+17 ;char *s15=malloc(sizeof(char)*len);sprintf(s15," <<<ArrayLiteral: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s15;}
				;
Elision	:
				 Elision ',' 	{int len=strlen($<c>1)+strlen($<c>2)+7+9 ;char *s16=malloc(sizeof(char)*len);sprintf(s16," <<<Elision: %s %s >>>",$<c>1,$<c>2);$<c>$=s16;}
				| 
	{$<c>$="EMPTY";}
				;
ElementList	:
				 Elision AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s18=malloc(sizeof(char)*len);sprintf(s18," <<<ElementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s18;}
				|  ElementList ',' Elision AssignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+15 ;char *s19=malloc(sizeof(char)*len);sprintf(s19," <<<ElementList: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s19;}
				;
ObjectLiteral	:
				 '{' PropertyNameAndValueList  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s20=malloc(sizeof(char)*len);sprintf(s20," <<<ObjectLiteral: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s20;}
				|  '{' PropertyNameAndValueList  ',' '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+17 ;char *s21=malloc(sizeof(char)*len);sprintf(s21," <<<ObjectLiteral: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s21;}
				;
PropertyNameAndValueList	:
				 PropertyNameAndValueList  ',' PropertyAssignment 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s22=malloc(sizeof(char)*len);sprintf(s22," <<<PropertyNameAndValueList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s22;}
				| PropertyAssignment
	{$<c>$=$<c>1;}
				;
PropertyAssignment	:
				 PropertyName ':' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s24=malloc(sizeof(char)*len);sprintf(s24," <<<PropertyAssignment: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s24;}
				| "get"PropertyName '(' ')' '{' FunctionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s25=malloc(sizeof(char)*len);sprintf(s25," <<<PropertyAssignment: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s25;}
				| "set"PropertyName '(' Identifier ')' '{' FunctionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s26=malloc(sizeof(char)*len);sprintf(s26," <<<PropertyAssignment: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s26;}
				;
PropertyName	:
				 Identifier 	{$<c>$=$<c>1;}
				| NumericLiteral 	{$<c>$=$<c>1;}
				| StringLiteral
	{$<c>$=$<c>1;}
				;
MemberExpression	:
				 PrimaryExpression 	{$<c>$=$<c>1;}
				| FunctionExpression 	{$<c>$=$<c>1;}
				| MemberExpression '[' Expression ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+20 ;char *s32=malloc(sizeof(char)*len);sprintf(s32," <<<MemberExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s32;}
				| MemberExpression '.' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s33=malloc(sizeof(char)*len);sprintf(s33," <<<MemberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s33;}
				| new MemberExpression Arguments
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+19 ;char *s34=malloc(sizeof(char)*len);sprintf(s34," <<<MemberExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s34;}
				;
NewExpression	:
				 new NewExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<NewExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s35;}
				| MemberExpression
	{$<c>$=$<c>1;}
				;
CallExpression	:
				 MemberExpression Arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s37=malloc(sizeof(char)*len);sprintf(s37," <<<CallExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s37;}
				| CallExpression Arguments 	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s38=malloc(sizeof(char)*len);sprintf(s38," <<<CallExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s38;}
				| CallExpression '[' Expression ']' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+18 ;char *s39=malloc(sizeof(char)*len);sprintf(s39," <<<CallExpression: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s39;}
				| CallExpression '.' Identifier
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<CallExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s40;}
				;
Arguments	:
				 '(' ArgumentList ')' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s41=malloc(sizeof(char)*len);sprintf(s41," <<<Arguments: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s41;}
				| '(' ')'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<Arguments: %s %s >>>",$<c>1,$<c>2);$<c>$=s42;}
				;
ArgumentList	:
				 ArgumentList ',' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<ArgumentList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s43;}
				| AssignmentExpression
	{$<c>$=$<c>1;}
				;
LeftHandSideExpression	:
				 NewExpression 	{$<c>$=$<c>1;}
				| CallExpression 
	{$<c>$=$<c>1;}
				;
UnaryExpression	:
				 delete UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s47=malloc(sizeof(char)*len);sprintf(s47," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s47;}
				| void UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s48=malloc(sizeof(char)*len);sprintf(s48," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s48;}
				| typeof UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s49;}
				| "++" UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s50=malloc(sizeof(char)*len);sprintf(s50," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s50;}
				| "--" UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s51=malloc(sizeof(char)*len);sprintf(s51," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s51;}
				| '+' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s52;}
				| '-' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s53=malloc(sizeof(char)*len);sprintf(s53," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s53;}
				| '~' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s54;}
				| '!' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s55=malloc(sizeof(char)*len);sprintf(s55," <<<UnaryExpression: %s %s >>>",$<c>1,$<c>2);$<c>$=s55;}
				| LeftHandSideExpression
	{$<c>$=$<c>1;}
				;
MultiplicativeExpression	:
				 MultiplicativeExpression '*' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s57=malloc(sizeof(char)*len);sprintf(s57," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s57;}
				| MultiplicativeExpression '/' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s58;}
				| MultiplicativeExpression '%' UnaryExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+27 ;char *s59=malloc(sizeof(char)*len);sprintf(s59," <<<MultiplicativeExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s59;}
				| UnaryExpression
	{$<c>$=$<c>1;}
				;
AdditiveExpression	:
				 AdditiveExpression '+' MultiplicativeExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s61=malloc(sizeof(char)*len);sprintf(s61," <<<AdditiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s61;}
				| AdditiveExpression '-' MultiplicativeExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s62=malloc(sizeof(char)*len);sprintf(s62," <<<AdditiveExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s62;}
				| MultiplicativeExpression
	{$<c>$=$<c>1;}
				;
ShiftExpression	:
				 ShiftExpression "<<" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s64=malloc(sizeof(char)*len);sprintf(s64," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s64;}
				| ShiftExpression ">>" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s65;}
				| ShiftExpression ">>>" AdditiveExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s66=malloc(sizeof(char)*len);sprintf(s66," <<<ShiftExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s66;}
				| AdditiveExpression
	{$<c>$=$<c>1;}
				;
RelationalExpression	:
				 RelationalExpression '<' ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s68=malloc(sizeof(char)*len);sprintf(s68," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s68;}
				| RelationalExpression '>' ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s69=malloc(sizeof(char)*len);sprintf(s69," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s69;}
				| RelationalExpression "<=" ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s70=malloc(sizeof(char)*len);sprintf(s70," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s70;}
				| RelationalExpression ">=" ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s71=malloc(sizeof(char)*len);sprintf(s71," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s71;}
				| RelationalExpression instanceof ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s72=malloc(sizeof(char)*len);sprintf(s72," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s72;}
				| RelationalExpression in ShiftExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s73=malloc(sizeof(char)*len);sprintf(s73," <<<RelationalExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s73;}
				| ShiftExpression
	{$<c>$=$<c>1;}
				;
EqualityExpression	:
				 EqualityExpression "==" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s75=malloc(sizeof(char)*len);sprintf(s75," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s75;}
				| EqualityExpression "!=" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s76=malloc(sizeof(char)*len);sprintf(s76," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s76;}
				| EqualityExpression "===" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s77=malloc(sizeof(char)*len);sprintf(s77," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s77;}
				| EqualityExpression "!==" RelationalExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+21 ;char *s78=malloc(sizeof(char)*len);sprintf(s78," <<<EqualityExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s78;}
				| RelationalExpression
	{$<c>$=$<c>1;}
				;
BitwiseANDExpression	:
				 BitwiseANDExpression '&' EqualityExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s80=malloc(sizeof(char)*len);sprintf(s80," <<<BitwiseANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s80;}
				| EqualityExpression
	{$<c>$=$<c>1;}
				;
BitwiseXORExpression	:
				 BitwiseXORExpression '^' BitwiseANDExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s82=malloc(sizeof(char)*len);sprintf(s82," <<<BitwiseXORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s82;}
				| BitwiseANDExpression
	{$<c>$=$<c>1;}
				;
BitwiseORExpression	:
				  BitwiseORExpression '#' BitwiseXORExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s84=malloc(sizeof(char)*len);sprintf(s84," <<<BitwiseORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s84;}
				| BitwiseXORExpression
	{$<c>$=$<c>1;}
				;
LogicalANDExpression	:
				 LogicalANDExpression "&&" BitwiseORExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s86=malloc(sizeof(char)*len);sprintf(s86," <<<LogicalANDExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s86;}
				| BitwiseORExpression   
	{$<c>$=$<c>1;}
				;
LogicalORExpression	:
				 LogicalORExpression "##" LogicalANDExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s88=malloc(sizeof(char)*len);sprintf(s88," <<<LogicalORExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s88;}
				| LogicalANDExpression
	{$<c>$=$<c>1;}
				;
ConditionalExpression	:
				 LogicalORExpression '?' AssignmentExpression ':' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+26 ;char *s90=malloc(sizeof(char)*len);sprintf(s90," <<<ConditionalExpression: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s90;}
				| LogicalORExpression
	{$<c>$=$<c>1;}
				;
AssignmentExpression	:
				 ConditionalExpression 	{$<c>$=$<c>1;}
				| LeftHandSideExpression '=' AssignmentExpression 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s93=malloc(sizeof(char)*len);sprintf(s93," <<<AssignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s93;}
				| LeftHandSideExpression AssignmentOperator AssignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+23 ;char *s94=malloc(sizeof(char)*len);sprintf(s94," <<<AssignmentExpression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s94;}
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
Expression	:
				 AssignmentExpression 	{$<c>$=$<c>1;}
				| AssignmentExpression ',' Expression
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s106=malloc(sizeof(char)*len);sprintf(s106," <<<Expression: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s106;}
				;
Statement	:
				 Block 	{$<c>$=$<c>1;}
				| VariableStatement 	{$<c>$=$<c>1;}
				| EmptyStatement 	{$<c>$=$<c>1;}
				| Expression 	{$<c>$=$<c>1;}
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
				 '{' StatementList '}'	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+8 ;char *s122=malloc(sizeof(char)*len);sprintf(s122," <<<Block: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s122;}
				| EmptyBlock
	{$<c>$=$<c>1;}
				;
EmptyBlock	:
				 '{' '}' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+12 ;char *s124=malloc(sizeof(char)*len);sprintf(s124," <<<EmptyBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s124;}
				;
StatementList	:
				 Statement 	{$<c>$=$<c>1;}
				| StatementList Statement
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s126=malloc(sizeof(char)*len);sprintf(s126," <<<StatementList: %s %s >>>",$<c>1,$<c>2);$<c>$=s126;}
				;
VariableStatement	:
				 var VariableDeclarationList ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s127=malloc(sizeof(char)*len);sprintf(s127," <<<VariableStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s127;}
				;
VariableDeclarationList	:
				 VariableDeclarationList  ',' VariableDeclaration 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+26 ;char *s128=malloc(sizeof(char)*len);sprintf(s128," <<<VariableDeclarationList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s128;}
				| VariableDeclaration
	{$<c>$=$<c>1;}
				;
VariableDeclaration	:
				 Identifier  	{$<c>$=$<c>1;}
				| Identifier Initialiser 
	{int len=strlen($<c>1)+strlen($<c>2)+7+21 ;char *s131=malloc(sizeof(char)*len);sprintf(s131," <<<VariableDeclaration: %s %s >>>",$<c>1,$<c>2);$<c>$=s131;}
				;
Initialiser	:
				 '=' AssignmentExpression
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s132=malloc(sizeof(char)*len);sprintf(s132," <<<Initialiser: %s %s >>>",$<c>1,$<c>2);$<c>$=s132;}
				;
EmptyStatement	:
				 ';'
	{$<c>$=$<c>1;}
				;
IfStatement	:
				  if '(' Expression ')' Statement else Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+18 ;char *s134=malloc(sizeof(char)*len);sprintf(s134," <<<IfStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s134;}
				| if '(' Expression ')' Statement   
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+16 ;char *s135=malloc(sizeof(char)*len);sprintf(s135," <<<IfStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s135;}
				;
IterationStatement	:
				 do Statement while '(' Expression ')' ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s136=malloc(sizeof(char)*len);sprintf(s136," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s136;}
				| while '(' Expression ')' Statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+23 ;char *s137=malloc(sizeof(char)*len);sprintf(s137," <<<IterationStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s137;}
				| for '(' Expression ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s138=malloc(sizeof(char)*len);sprintf(s138," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s138;}
				| for '(' ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s139=malloc(sizeof(char)*len);sprintf(s139," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s139;}
				| for '(' Expression ';'  ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s140=malloc(sizeof(char)*len);sprintf(s140," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s140;}
				| for '(' ';' ';' Expression ')' Statement  	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s141=malloc(sizeof(char)*len);sprintf(s141," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s141;}
				| for '(' Expression ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s142=malloc(sizeof(char)*len);sprintf(s142," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s142;}
				| for '(' Expression ';'  ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s143=malloc(sizeof(char)*len);sprintf(s143," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s143;}
				| for '('  ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s144=malloc(sizeof(char)*len);sprintf(s144," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s144;}
				| for '(' ';' ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s145=malloc(sizeof(char)*len);sprintf(s145," <<<IterationStatement: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s145;}
				| for '(' var VariableDeclarationList ';' Expression ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+strlen($<c>10)+7+28 ;char *s146=malloc(sizeof(char)*len);sprintf(s146," <<<IterationStatement: %s %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9,$<c>10);$<c>$=s146;}
				| for '(' var VariableDeclarationList ';' Expression ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s147=malloc(sizeof(char)*len);sprintf(s147," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s147;}
				| for '(' var VariableDeclarationList ';' ';' Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+strlen($<c>9)+7+27 ;char *s148=malloc(sizeof(char)*len);sprintf(s148," <<<IterationStatement: %s %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8,$<c>9);$<c>$=s148;}
				| for '(' var VariableDeclarationList ';'  ';'  ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s149=malloc(sizeof(char)*len);sprintf(s149," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s149;}
				| for '(' LeftHandSideExpression in Expression ')' Statement 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s150=malloc(sizeof(char)*len);sprintf(s150," <<<IterationStatement: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s150;}
				| for '(' var VariableDeclaration in Expression ')' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+26 ;char *s151=malloc(sizeof(char)*len);sprintf(s151," <<<IterationStatement: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s151;}
				;
ContinueStatement	:
				 continue Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s152=malloc(sizeof(char)*len);sprintf(s152," <<<ContinueStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s152;}
				| continue ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s153=malloc(sizeof(char)*len);sprintf(s153," <<<ContinueStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s153;}
				;
BreakStatement	:
				 break Identifier ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s154=malloc(sizeof(char)*len);sprintf(s154," <<<BreakStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s154;}
				| break ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+16 ;char *s155=malloc(sizeof(char)*len);sprintf(s155," <<<BreakStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s155;}
				;
ReturnStatement	:
				 return Expression ';' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+18 ;char *s156=malloc(sizeof(char)*len);sprintf(s156," <<<ReturnStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s156;}
				| return ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+17 ;char *s157=malloc(sizeof(char)*len);sprintf(s157," <<<ReturnStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s157;}
				;
WithStatement	:
				 with '(' Expression ')' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+18 ;char *s158=malloc(sizeof(char)*len);sprintf(s158," <<<WithStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s158;}
				;
SwitchStatement	:
				 switch '(' Expression ')' CaseBlock
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s159=malloc(sizeof(char)*len);sprintf(s159," <<<SwitchStatement: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s159;}
				;
CaseBlock	:
				 '{' CaseClauses  DefaultClause CaseClauses  '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+14 ;char *s160=malloc(sizeof(char)*len);sprintf(s160," <<<CaseBlock: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s160;}
				| '{' CaseClauses DefaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s161=malloc(sizeof(char)*len);sprintf(s161," <<<CaseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s161;}
				| '{' CaseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s162=malloc(sizeof(char)*len);sprintf(s162," <<<CaseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s162;}
				| '{' DefaultClause CaseClauses '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+13 ;char *s163=malloc(sizeof(char)*len);sprintf(s163," <<<CaseBlock: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s163;}
				| '{' DefaultClause '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+12 ;char *s164=malloc(sizeof(char)*len);sprintf(s164," <<<CaseBlock: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s164;}
				| '{' '}'
	{int len=strlen($<c>1)+strlen($<c>2)+7+11 ;char *s165=malloc(sizeof(char)*len);sprintf(s165," <<<CaseBlock: %s %s >>>",$<c>1,$<c>2);$<c>$=s165;}
				;
CaseClauses	:
				 CaseClause 	{$<c>$=$<c>1;}
				| CaseClauses CaseClause
	{int len=strlen($<c>1)+strlen($<c>2)+7+13 ;char *s167=malloc(sizeof(char)*len);sprintf(s167," <<<CaseClauses: %s %s >>>",$<c>1,$<c>2);$<c>$=s167;}
				;
CaseClause	:
				 case Expression ':' StatementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+14 ;char *s168=malloc(sizeof(char)*len);sprintf(s168," <<<CaseClause: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s168;}
				| case Expression ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+13 ;char *s169=malloc(sizeof(char)*len);sprintf(s169," <<<CaseClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s169;}
				;
DefaultClause	:
				 default ':' StatementList 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+16 ;char *s170=malloc(sizeof(char)*len);sprintf(s170," <<<DefaultClause: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s170;}
				| default ':' 
	{int len=strlen($<c>1)+strlen($<c>2)+7+15 ;char *s171=malloc(sizeof(char)*len);sprintf(s171," <<<DefaultClause: %s %s >>>",$<c>1,$<c>2);$<c>$=s171;}
				;
LabelledStatement	:
				 Identifier ':' Statement
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+20 ;char *s172=malloc(sizeof(char)*len);sprintf(s172," <<<LabelledStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s172;}
				;
ThrowStatement	:
				 throw Expression ';'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+17 ;char *s173=malloc(sizeof(char)*len);sprintf(s173," <<<ThrowStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s173;}
				;
TryStatement	:
				 try Block CatchProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s174=malloc(sizeof(char)*len);sprintf(s174," <<<TryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s174;}
				| try Block FinallyProduction 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+15 ;char *s175=malloc(sizeof(char)*len);sprintf(s175," <<<TryStatement: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s175;}
				| try Block CatchProduction FinallyProduction
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+7+16 ;char *s176=malloc(sizeof(char)*len);sprintf(s176," <<<TryStatement: %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4);$<c>$=s176;}
				;
CatchProduction	:
				 catch '(' Identifier ')' Block
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+7+20 ;char *s177=malloc(sizeof(char)*len);sprintf(s177," <<<CatchProduction: %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5);$<c>$=s177;}
				;
FinallyProduction	:
				 finally block
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s178=malloc(sizeof(char)*len);sprintf(s178," <<<FinallyProduction: %s %s >>>",$<c>1,$<c>2);$<c>$=s178;}
				;
DebuggerStatement	:
				 debugger ';'
	{int len=strlen($<c>1)+strlen($<c>2)+7+19 ;char *s179=malloc(sizeof(char)*len);sprintf(s179," <<<DebuggerStatement: %s %s >>>",$<c>1,$<c>2);$<c>$=s179;}
				;
FunctionDeclaration	:
				 function Identifier '(' FormalParameterList ')' '{' FunctionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+strlen($<c>8)+7+27 ;char *s180=malloc(sizeof(char)*len);sprintf(s180," <<<FunctionDeclaration: %s %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7,$<c>8);$<c>$=s180;}
				| function Identifier '('  ')' '{' FunctionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+26 ;char *s181=malloc(sizeof(char)*len);sprintf(s181," <<<FunctionDeclaration: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s181;}
				;
FunctionExpression	:
				 function '(' FormalParameterList ')' '{' FunctionBody '}' 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+strlen($<c>7)+7+25 ;char *s182=malloc(sizeof(char)*len);sprintf(s182," <<<FunctionExpression: %s %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6,$<c>7);$<c>$=s182;}
				| function  '(' ')' '{' FunctionBody '}'
	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+strlen($<c>4)+strlen($<c>5)+strlen($<c>6)+7+24 ;char *s183=malloc(sizeof(char)*len);sprintf(s183," <<<FunctionExpression: %s %s %s %s %s %s >>>",$<c>1,$<c>2,$<c>3,$<c>4,$<c>5,$<c>6);$<c>$=s183;}
				;
FormalParameterList	:
				 FormalParameterList ',' Identifier 	{int len=strlen($<c>1)+strlen($<c>2)+strlen($<c>3)+7+22 ;char *s184=malloc(sizeof(char)*len);sprintf(s184," <<<FormalParameterList: %s %s %s >>>",$<c>1,$<c>2,$<c>3);$<c>$=s184;}
				| Identifier
	{$<c>$=$<c>1;}
				;
FunctionBody	:
				 SourceElements 	{$<c>$=$<c>1;}
				| 
	{$<c>$="EMPTY";}
				;

%%
int main()
{
yyparse();
}