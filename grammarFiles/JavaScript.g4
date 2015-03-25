program : sourceElements | 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement

block : { statementList } |  { } 

statementList : statement | statement statementList

variableStatement : var variableDeclarationList ;

variableDeclarationList : variableDeclaration , variableDeclarationList | variableDeclaration

variableDeclaration : identifier initialiser |  identifier

initialiser : = singleExpression

emptyStatement : ;

expressionStatement : expressionSequence

ifStatement : if ( expressionSequence ) statement else statement | if ( expressionSequence ) statement 

iterationStatement : do statement while ( expressionSequence ) ; | while ( expressionSequence ) statement | for ( ; ; ) statement | for ( ; ; expressionSequence ) statement | for ( ; expressionSequence ; ) statement | for ( ; expressionSequence ; expressionSequence ) statement | for ( expressionSequence ; ; ) statement | for ( expressionSequence ; ; expressionSequence ) statement | for ( expressionSequence ; expressionSequence ; ) statement | for ( expressionSequence ; expressionSequence ; expressionSequence ) statement | for ( var variableDeclarationList ; ; ) statement | for ( var variableDeclarationList ; ; expressionSequence ) statement | for ( var variableDeclarationList ; expressionSequence ; ) statement | for ( var variableDeclarationList ; expressionSequence ; expressionSequence ) statement | for ( singleExpression In expressionSequence ) statement | for ( var variableDeclaration In expressionSequence ) statement

continueStatement : continue identifier ; | continue ;

breakStatement : break identifier ; | break ;

returnStatement : return expressionSequence ; | return ;

withStatement : with ( expressionSequence ) statement

switchStatement : switch ( expressionSequence ) caseBlock

caseBlock : { caseClauses defaultClause caseClauses } | { caseClauses defaultClause } | { caseClauses } | { defaultClause caseClauses } |{ defaultClause } | { } 

caseClauses : caseClause | caseClause caseClauses

caseClause : case expressionSequence : statementList |  case expressionSequence :

defaultClause : default : statementList | default : 

labelledStatement : identifier : statement

throwStatement : throw expressionSequence ;

tryStatement : try block catchProduction | try block finallyProduction | try block catchProduction finallyProduction

catchProduction : catch ( identifier ) block

finallyProduction : finally block

debuggerStatement : debugger ;

functionDeclaration : function identifier ( formalParameterList ) { functionBody } | function identifier ( ) { functionBody }

formalParameterList : identifier , formalParameterList | identifier

functionExpression	: function ( formalParameterList ) { functionBody }	| function  ( ) { functionBody }

functionBody : sourceElements |
    
arrayLiteral : [ elementList , elision ] | [ elementList , ] |[ elementList ] | [ , elision ] | [ , ] |[ elision ] | [] | [elementList elision]
 
elementList : elision singleExpression elementList | elision singleExpression | singleExpression |elision elementList

elision : , | , elision

objectLiteral : { } | { propertyNameAndValueList } |{ propertyNameAndValueList ,  }

propertyNameAndValueList : propertyAssignment , propertyNameAndValueList | propertyAssignment
    
propertyAssignment : propertyName : singleExpression | get identifier ( ) { functionBody }| set identifier ( propertySetParameterList ) { functionBody }
    
propertyName : identifierName | StringLiteral | numericLiteral
    
propertySetParameterList : identifier

arguments : ( argumentList ) |  ( )
    
argumentList : singleExpression , argumentList | singleExpression 
    
expressionSequence : singleExpression expressionSequence | singleExpression

singleExpression : functionExpression | singleExpression [ expressionSequence ] | singleExpression . identifierName | singleExpression arguments | new singleExpression arguments | new singleExpression | singleExpression ++ | singleExpression -- | delete singleExpression | void singleExpression | typeof singleExpression | ++ singleExpression | -- singleExpression | + singleExpression | - singleExpression | ~ singleExpression | ! singleExpression | singleExpression * singleExpression | singleExpression / singleExpression | singleExpression % singleExpression | singleExpression + singleExpression | singleExpression - singleExpression | singleExpression << singleExpression | singleExpression >> singleExpression | singleExpression >>> singleExpression | singleExpression < singleExpression | singleExpression > singleExpression | singleExpression <= singleExpression | singleExpression >= singleExpression | singleExpression instanceof singleExpression | singleExpression in singleExpression | singleExpression == singleExpression | singleExpression != singleExpression | singleExpression === singleExpression | singleExpression !== singleExpression | singleExpression & singleExpression | singleExpression ^ singleExpression | singleExpression | singleExpression | singleExpression && singleExpression | singleExpression ## singleExpression | singleExpression ? singleExpression : singleExpression | singleExpression = expressionSequence | singleExpression assignmentOperator expressionSequence | this | identifier | literal | arrayLiteral | objectLiteral | ( expressionSequence )

assignmentOperator : *= | /= | %= | += | -= | <<= | >>= | >>>= | &= | ^= | |=

literal : NullLiteral | BooleanLiteral | StringLiteral | RegularExpressionLiteral | numericLiteral

numericLiteral : DecimalLiteral | HexIntegerLiteral | OctalIntegerLiteral

identifierName : identifier | reservedWord

reservedWord : keyword | futureReservedWord | NullLiteral | BooleanLiteral

keyword : break | do | instanceof | typeof | case | else | new | var | catch | finally | return | void | continue | for | switch | while | debugger | function | this | with | default | if | throw | delete | in | try

futureReservedWord : class | enum | extends | super | const | export | import | implements | let | private | public | interface | package | protected | static | yield

NullLiteral : null

BooleanLiteral : true | false

identifier : Ident

