program : sourceElements | 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration
	
functionDeclaration	: function  identifier  formalParameterList  functionBody
	
functionExpression	: function  identifier  formalParameterList  functionBody | function  formalParameterList  functionBody
	
formalParameterList	: ( identifier , formalParameterList  )| identifier

formalParameterList : identifier , formalParameterList| identifier

functionBody	: {  sourceElements  }

statement	: statementBlock	| variableStatement	| emptyStatement	| expressionStatement	| ifStatement	| iterationStatement	| continueStatement	| breakStatement	| returnStatement	| withStatement	| labelledStatement	| switchStatement	| throwStatement	| tryStatement		

statementBlock	: {  statementList } | {  }
	
statementList : statement | statement statementList
	
variableStatement : var  variableDeclarationList eos

variableDeclarationList : variableDeclaration , variableDeclarationList | variableDeclaration
	
variableDeclarationListNoIn : variableDeclaration , variableDeclarationListNoIn | variableDeclaration
	
variableDeclaration	: identifier  initialiser | identifier
	
variableDeclarationNoIn	: identifier  initialiserNoIn | identifier
	
initialiser	: =  assignmentExpression
	
initialiserNoIn	: =  assignmentExpressionNoIn
	
emptyStatement	: ;
	
expressionStatement	: expression  eos
	
ifStatement	: if  (  expression  )  statement else  statement | if  (  expression  )  statement 

iterationStatement	: doWhileStatement	| whileStatement	| forStatement	| forInStatement
	
doWhileStatement	: do  statement  while  ( expression ) eos 

eos : | ;	

whileStatement	: while  (  expression  )  statement
	
forStatement : for  ( forStatementInitialiserPart  ;  expression  ;  expression  )  statement | for  ( forStatementInitialiserPart  ;  expression  ;    )  statement | for  ( forStatementInitialiserPart  ;    ;    )  statement | for  ( forStatementInitialiserPart  ;    ;  expression  )  statement | for  (   ;  expression  ;  expression  )  statement | for  (   ;  expression  ;    )  statement | for  (   ;    ;  expression  )  statement | for  (   ;    ;    )  statement	

forStatementInitialiserPart	: expressionNoIn	| var  variableDeclarationListNoIn
	
forInStatement	: for  (  forInStatementInitialiserPart  in  expression  )  statement
	
forInStatementInitialiserPart	: leftHandSideExpression	| var  variableDeclarationNoIn

continueStatement	: continue identifier eos | continue eos

breakStatement	: break identifier eos | break eos

returnStatement	: return expression eos | return
	
withStatement	: with  (  expression  )  statement

labelledStatement	: identifier  :  statement
	
switchStatement	: switch  (  expression  )  caseBlock
	
caseBlock : { caseClause1 defaultClause caseClause1  }	| { caseClause1  }

caseClause1 : caseClause caseClause1 | caseClause

caseClause	: case  expression  :  statementList | case  expression  :
	
defaultClause	: default  :  statementList| default  : 
	
throwStatement	: throw expression eos

tryStatement	: try  statementBlock  finallyClause | try  statementBlock  catchClause | try  statementBlock  catchClause  finallyClause
       
catchClause	: catch  (  identifier  )  statementBlock
	
finallyClause	: finally  statementBlock

expression	: assignmentExpression ,  expression
	
expressionNoIn	: assignmentExpressionNoIn ,  expressionNoIn
	
assignmentExpression : conditionalExpression | leftHandSideExpression  assignmentOperator  assignmentExpression
	
assignmentExpressionNoIn	: conditionalExpressionNoIn	| leftHandSideExpression  assignmentOperator  assignmentExpressionNoIn
	
leftHandSideExpression	: callExpression	| newExpression
	
newExpression	: memberExpression	| new  newExpression
	
memberExpression: primaryExpression memberExpression1 | functionExpression memberExpression1 | new  memberExpression  arguments memberExpression1 

memberExpression1 :  memberExpressionSuffix | memberExpressionSuffix memberExpression1
	
memberExpressionSuffix	: indexSuffix	| propertyReferenceSuffix

callExpression	: memberExpression  arguments  | memberExpression  arguments callExpression1 

callExpression1 : callExpressionSuffix | callExpressionSuffix callExpression1 
	
callExpressionSuffix	: arguments	| indexSuffix	| propertyReferenceSuffix

arguments	: ( argumentList )

argumentList : assignmentExpression |  assignmentExpression ,  argumentList 
	
indexSuffix	: [  expression  ]
	
propertyReferenceSuffix	: .  identifier
	
assignmentOperator	: = | *= | /= | %= | += | -= | <<= | >>= | >>>= | &= | ^= | #=

conditionalExpression	: logicalORExpression ?  assignmentExpression  :  assignmentExpression | logicalORExpression

conditionalExpressionNoIn	: logicalORExpressionNoIn ?  assignmentExpressionNoIn  :  assignmentExpressionNoIn | logicalORExpressionNoIn

logicalORExpression	: logicalANDExpression ##  logicalORExpression | logicalANDExpression
	
logicalORExpressionNoIn	: logicalANDExpressionNoIn ##  logicalORExpressionNoIn | logicalANDExpressionNoIn
	
logicalANDExpression	: bitwiseORExpression &&  logicalANDExpression| bitwiseORExpression
	
logicalANDExpressionNoIn	: bitwiseORExpressionNoIn &&  logicalANDExpressionNoIn | bitwiseORExpressionNoIn
	
bitwiseORExpression	: bitwiseXORExpression | bitwiseXORExpression # bitwiseORExpression 
	
bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn #  bitwiseORExpressionNoIn | bitwiseXORExpressionNoIn
	
bitwiseXORExpression	: bitwiseANDExpression ^  bitwiseXORExpression | bitwiseANDExpression
	
bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ^  bitwiseXORExpressionNoIn | bitwiseANDExpressionNoIn
	
bitwiseANDExpression	: equalityExpression &  bitwiseANDExpression | equalityExpression
	
bitwiseANDExpressionNoIn	: equalityExpressionNoIn &  bitwiseANDExpressionNoIn | equalityExpressionNoIn
	
equalityExpression	: relationalExpression | relationalExpression == equalityExpression | relationalExpression = equalityExpression | relationalExpression === equalityExpression | relationalExpression == equalityExpression

equalityExpressionNoIn	: relationalExpressionNoIn | relationalExpressionNoIn  == equalityExpressionNoIn | relationalExpressionNoIn = equalityExpressionNoIn | relationalExpressionNoIn === equalityExpressionNoIn | relationalExpressionNoIn == equalityExpressionNoIn
	
relationalExpression : shiftExpression | shiftExpression < relationalExpression | shiftExpression > relationalExpression | shiftExpression <= relationalExpression | shiftExpression >= relationalExpression | shiftExpression instanceof relationalExpression | shiftExpression in relationalExpression

relationalExpressionNoIn	: shiftExpression | shiftExpression < relationalExpressionNoIn | shiftExpression > relationalExpressionNoIn | shiftExpression <= relationalExpressionNoIn | shiftExpression >= relationalExpressionNoIn | shiftExpression instanceof relationalExpressionNoIn

shiftExpression	: additiveExpression | additiveExpression << shiftExpression | additiveExpression >>  shiftExpression | additiveExpression >>> shiftExpression

additiveExpression	: multiplicativeExpression | multiplicativeExpression + additiveExpression | multiplicativeExpression -  additiveExpression

multiplicativeExpression	: unaryExpression | unaryExpression * multiplicativeExpression| unaryExpression /  multiplicativeExpression | unaryExpression %  multiplicativeExpression

unaryExpression	: postfixExpression	| delete unaryExpression | void unaryExpression | typeof unaryExpression | ++ unaryExpression | -- unaryExpression | + unaryExpression | - unaryExpression | ~ unaryExpression |  unaryExpression
	
postfixExpression	: leftHandSideExpression ++ | leftHandSideExpression -- | leftHandSideExpression

primaryExpression	: this	| identifier	| literal	| arrayLiteral	| objectLiteral	| (  expression  )
	
arrayLiteral	: [  assignmentExpression arrayLiteral1  ] | [  arrayLiteral1  ]

arrayLiteral1	:   | , assignmentExpression arrayLiteral1 | , 
       
objectLiteral	: {  propertyNameAndValue1 }
	
propertyNameAndValue1 : propertyNameAndValue | propertyNameAndValue ,  propertyNameAndValue1  
	
propertyNameAndValue	: propertyName  :  assignmentExpression

propertyName	: identifier	| StringLiteral	| NumericLiteral

literal	: null	| true	| false	| StringLiteral	| NumericLiteral	
	
NumericLiteral	: DecimalLiteral	| HexIntegerLiteral
	
identifier : Ident

keyword : break | do | instanceof | typeof | case | else | new | var | catch | finally | return | void | continue | for | switch | while | debugger | function | this | with | default | if | throw | delete | in | try | null | true | false | class | enum | extends | super | const | export | import | implements | let | private | public | interface | package | protected | static | yield

