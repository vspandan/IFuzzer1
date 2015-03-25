program	: sourceElements |

sourceElements	: sourceElement | sourceElement sourceElements

sourceElement	: statement	| functionDeclaration

primaryExpression	: This	| Identifier	| literal	| arrayLiteral	| objectLiteral	| ( expression )

arrayLiteral	: [ ]	| [ elision ]	| [ elementList ]	| [ elementList , ]	| [ elementList , elision ]

elementList	: assignmentExpression elementList	| elision assignmentExpression

elision	: , | , elision	

objectLiteral	: {   }	| { propertyNameAndValueList }	| { propertyNameAndValueList , }

propertyNameAndValueList	: propertyAssignment	| propertyAssignment , propertyNameAndValueList

propertyAssignment 	: propertyName : assignmentExpression	| Get propertyName ( ) { functionBody }	| Set propertyName ( propertySetParameterList ) { functionBody }

propertyName	: identifierName	| StringLiteral	| numericLiteral
	
propertySetParameterList	: Identifier

memberExpression	: primaryExpression	| functionExpression	| memberExpression [ expression ]	| memberExpression . identifierName	| New memberExpression arguments
	
newExpression	: memberExpression	| New newExpression
	
callExpression	: memberExpression arguments	| callExpression arguments	| callExpression [ expression ]	| callExpression . identifierName
	
arguments	: ( )	| ( argumentList )
	
argumentList : assignmentExpression	| assignmentExpression , argumentList
	
leftHandSideExpression : newExpression	| callExpression

arthExpression : arthExpression * arthExpression 	| arthExpression / arthExpression	| arthExpression % arthExpression	| arthExpression + arthExpression| arthExpression - arthExpression  | arthExpression << arthExpression | arthExpression >> arthExpression | arthExpression >>> arthExpression | arthExpression < arthExpression | arthExpression > arthExpression | arthExpression <= arthExpression | arthExpression >= arthExpression | arthExpression instanceof arthExpression| arthExpression in arthExpression | arthExpression == arthExpression | arthExpression != arthExpression | arthExpression === arthExpression | arthExpression !== arthExpression | arthExpression & arthExpression | arthExpression ^ arthExpression | arthExpression # arthExpression | arthExpression && arthExpression | arthExpression ## arthExpression  | arthExpression ? assignmentExpression : assignmentExpression | leftHandSideExpression	| leftHandSideExpression ++ | leftHandSideExpression -- | Delete arthExpression	| Void arthExpression | Typeof arthExpression	| ++ arthExpression	| -- arthExpression	| + arthExpression	| - arthExpression	| ~ arthExpression	| ! arthExpression   

assignmentExpression	: arthExpression	| leftHandSideExpression = assignmentExpression	| leftHandSideExpression assignmentOperator assignmentExpression

assignmentOperator	: *=	| /=	| %=	| +=	| -=	| <<=	| >>=	| >>>= | &=	| ^=

expression	: assignmentExpression	| assignmentExpression , expression

statement 	: variableStatement	| block | emptyStatement	| expression	| ifStatement	| iterationStatement	| continueStatement	| breakStatement	| returnStatement	| withStatement	| labelledStatement	| switchStatement	| throwStatement	| tryStatement	| debuggerStatement

block	:  { } | { statementList }

statementList : statement | statement statementList

variableStatement : Var variableDeclarationList ;

variableDeclarationList : variableDeclaration | variableDeclaration , variableDeclarationList

variableDeclaration	: Identifier	| Identifier initialiser

initialiser : = assignmentExpression

emptyStatement	: EOS

ifStatement 	: If ( expression ) statement | If ( expression ) statement Else statement

iterationStatement 	: For ( ; ;  ) statement | For ( expression ; expression ; expression ) statement	| For ( ; expression ; expression ) statement	| For ( expression ;  ; expression ) statement	| For ( ; ; expression ) statement	| For ( expression ; expression ;  ) statement	| For ( expression ;  ;  ) statement	| For (  ; expression ;  ) statement | For ( Var variableDeclarationList ; expression ; expression ) statement	| For ( Var variableDeclarationList ; expression ;  ) statement	| For ( Var variableDeclarationList ; ; expression ) statement	| For ( Var variableDeclarationList ;  ;  ) statement	| For ( leftHandSideExpression In expression ) statement	| For ( Var variableDeclaration In expression ) statement | Do statement While ( expression ) ;	| While ( expression ) statement

continueStatement 	: Continue ; | Continue Identifier ;

breakStatement	:  Break ; | Break Identifier ;

returnStatement	: Return ; | Return expression ;

withStatement	: With ( expression ) statement

switchStatement	: Switch ( expression ) caseBlock

caseBlock	: { } | { caseClauses } | { caseClauses  defaultClause caseClauses  }	| { caseClauses defaultClause }	| { defaultClause caseClauses }	| { defaultClause } 

caseClauses	: caseClause | caseClause caseClauses

caseClause	: Case expression : statementList	| Case expression : 

defaultClause : Default : | Default : statementList 

labelledStatement	: Identifier : statement
	
throwStatement	: Throw expression ;

tryStatement	: Try block catchProduction	| Try block finallyProduction	| Try block catchProduction finallyProduction
	
catchProduction	: Catch ( Identifier ) block
	
finallyProduction	: Finally block
	
debuggerStatement	: Debugger ;

functionDeclaration	: Function Identifier (  ) { functionBody } | Function Identifier ( formalParameterList ) { functionBody }
	
functionExpression	: Function  ( ) { functionBody } | Function ( formalParameterList ) { functionBody }	| 
	
formalParameterList	: Identifier | Identifier , formalParameterList
	
functionBody :  | sourceElements

nullLiteral	: Null

booleanLiteral	: true | false

EOS : ; 

Null : null

Get : get

Set : set

numericLiteral	: DecimalLiteral | HexIntegerLiteral

identifierName	: StringLiteral	| reservedWord

reservedWord : keyword | futureReservedWord | nullLiteral | booleanLiteral

keyword : Break | Do | Instanceof | Typeof | Case | Else | New | Var | Catch | Finally | Return | Void | Continue | For | Switch | While | Debugger | Function | This | With | Default | If | Throw | Delete | In | Try

futureReservedWord : Class | Enum | Extends | Super | Const | Export | Import | Implements | Let | Private | Public | Interface | Package | Protected | Static | Yield
	
literal : nullLiteral	| booleanLiteral	| numericLiteral | StringLiteral	| RegularExpressionLiteral
	
Break      : break

Do         : do

Instanceof : instanceof

Typeof     : typeof

Case       : case

Else       : else

New        : new

Var        : var

Catch      : catch

Finally    : finally

Return     : return

Void       : void

Continue   : continue

For        : for

Switch     : switch

While      : while

Debugger   : debugger

Function   : function

This       : this

With       : with

Default    : default

If         : if

Throw      : throw

Delete     : delete

In         : in

Try        : try

Class   : class

Enum    : enum

Extends : extends

Super   : super

Const   : const

Export  : export

Import  : import

Implements : implements

Let        : let

Private    : private

Public     : public

Interface  : interface

Package    : package

Protected  : protected

Static     : static

Yield      : yield

Identifier 	: IdentifierStart IdentifierPart