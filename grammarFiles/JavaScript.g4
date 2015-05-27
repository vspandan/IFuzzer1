program : sourceElements | 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

functionDeclaration : function identifier ( formalParameterList ) { functionBody } | function identifier ( ) { functionBody }

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement | yieldExpression | elseStatement

yieldExpression : Yield expression | Yield

block : { statementList } |  { } 

statementList : statement | statement statementList

variableStatement : var variableDeclarationList | let variableDeclarationList | const variableDeclarationList ;

variableDeclarationList : variableDeclarationList  , variableDeclaration | variableDeclaration

variableDeclaration : identifier initialiser | arrayLiteral initialiser | objectLiteral initialiser | identifier | arrayLiteral | objectLiteral

initialiser : = assignmentExpression

emptyStatement :  ;

expressionStatement : expression

ifStatement : if ( expression ) statement elseStatement | if ( expression ) statement 

elseStatement : else statement

iterationStatement : do statement while ( expression ) ; | while ( expression ) statement | for ( ; ; ) statement | for ( ; ; expression ) statement | for ( ; expression ; ) statement | for ( ; expression ; expression ) statement | for ( expression ; ; ) statement | for ( expression ; ; expression ) statement | for ( expression ; expression ; ) statement | for ( expression ; expression ; expression ) statement | for ( var variableDeclarationList ; ; ) statement | for ( var variableDeclarationList ; ; expression ) statement | for ( var variableDeclarationList ; expression ; ) statement | for ( var variableDeclarationList ; expression ; expression ) statement |  for ( let variableDeclarationList ; ; ) statement | for ( let variableDeclarationList ; ; expression ) statement | for ( let variableDeclarationList ; expression ; ) statement | let ( var variableDeclarationList ; expression ; expression ) statement |  for ( const variableDeclarationList ; ; ) statement | for ( const variableDeclarationList ; ; expression ) statement | for ( const variableDeclarationList ; expression ; ) statement | for ( const variableDeclarationList ; expression ; expression ) statement | for each ( var leftHandSideExpression in expression ) statement  | for ( var leftHandSideExpression in expression ) statement  | for each ( let leftHandSideExpression in expression ) statement  | for ( let leftHandSideExpression in expression ) statement  | for each ( const leftHandSideExpression in expression ) statement  | for ( const leftHandSideExpression in expression ) statement | for ( const variableDeclarationList ; expression ; ) statement | for ( const variableDeclarationList ; expression ; expression ) statement | for each ( var leftHandSideExpression of expression ) statement  | for ( var leftHandSideExpression of expression ) statement  | for each ( let leftHandSideExpression of expression ) statement  | for ( let leftHandSideExpression of expression ) statement  | for each ( const leftHandSideExpression of expression ) statement  | for ( const leftHandSideExpression of expression ) statement 

continueStatement : continue identifier ; | continue ;

breakStatement : break identifier ; | break ;

returnStatement : return expression ; | return ;

withStatement : with ( expression ) statement

switchStatement : switch ( expression ) caseBlock

caseBlock : { caseClauses defaultClause caseClauses } | { caseClauses defaultClause } | { caseClauses } | { defaultClause caseClauses } |{ defaultClause } | { } 

caseClauses : caseClause | caseClause caseClauses

defaultClause : default : statementList | default : 

labelledStatement : identifier : statement

throwStatement : throw expression ;

tryStatement : try block catchProduction | try block finallyProduction | try block catchProduction finallyProduction

catchProduction : catchProduction catch ( identifier ) block | 

finallyProduction : finally block

debuggerStatement : debugger ;

formalParameterList : formalParameterList ',' formalParameter | formalParameter

formalParameter : identifier | arrayLiteral | objectLiteral

functionBody : sourceElements |
    
arrayLiteral : [ elementList , elision ] | [ elementList , ] |[ elementList ] | [ , elision ] | [ , ] |[ elision ] | [] | [elementList elision]

elementList : elision expression elementList | elision expression | expression |elision elementList

elision : , | , elision

objectLiteral : { } | { propertyNameAndValueList } |{ propertyNameAndValueList ,  }

propertyNameAndValueList : propertyAssignment , propertyNameAndValueList | propertyAssignment
    
propertyAssignment : propertyName | propertyName : assignmentExpression | get identifierName ( ) { functionBody } | set identifierName ( propertySetParameterList ) { functionBody }
    
propertyName : identifierName | StringLiteral | numericLiteral
    
propertySetParameterList : identifier

arguments : ( argumentList ) |  ( )
    
argumentList : expression , argumentList | expression 
    
expression : assignmentExpression expression | assignmentExpression | assignmentExpression for each ( identifier of expression ) statement | assignmentExpression for  ( identifier of expression ) statement | assignmentExpression for each ( identifier in expression ) statement | assignmentExpression for  ( identifier in expression ) statement | expression if ( expression ) | ( formalParameterList ) =>  expression | ( ) => expression | ( formalParameterList ) => statement | ( ) => statement | identifier => { statement }  | identifier => expression | let ( expression ) statement

assignmentExpression : yieldExpression | conditionalExpression | leftHandSideExpression  =  assignmentExpression | leftHandSideExpression assignmentOperator assignmentExpression

conditionalExpression : logicalORExpression | logicalORExpression  ?  assignmentExpression  :  assignmentExpression

logicalORExpression : logicalANDExpression | logicalORExpression  ##  logicalANDExpression

logicalANDExpression : bitwiseORExpression | logicalANDExpression  &&  bitwiseORExpression

bitwiseORExpression : bitwiseXORExpression | bitwiseORExpression  #  bitwiseXORExpression

bitwiseXORExpression : bitwiseANDExpression | bitwiseXORExpression  ^  bitwiseANDExpression

bitwiseANDExpression : equalityExpression | bitwiseANDExpression & equalityExpression

equalityExpression  : relationalExpression | equalityExpression  ==  relationalExpression | equalityExpression  !=  relationalExpression | equalityExpression  ===  relationalExpression | equalityExpression  !==  relationalExpression

relationalExpression  : shiftExpression | relationalExpression  <  shiftExpression | relationalExpression  >  shiftExpression | relationalExpression  <=  shiftExpression | relationalExpression  >=  shiftExpression | relationalExpression instanceof shiftExpression  | relationalExpression in shiftExpression

shiftExpression : additiveExpression | shiftExpression  <<  additiveExpression | shiftExpression  >>  additiveExpression | shiftExpression  >>>  additiveExpression
 
additiveExpression :  multiplicativeExpression | additiveExpression  +  multiplicativeExpression | additiveExpression  -  multiplicativeExpression

multiplicativeExpression :  unaryExpression | multiplicativeExpression  *  unaryExpression | multiplicativeExpression  /  unaryExpression | multiplicativeExpression  %  unaryExpression

unaryExpression :  postfixExpression | delete unaryExpression | void unaryExpression | typeof unaryExpression |  ++  unaryExpression |  --  unaryExpression | + unaryExpression |  -  unaryExpression |  ~  unaryExpression |  !  unaryExpression

postfixExpression :  leftHandSideExpression | leftHandSideExpression ++ | leftHandSideExpression --

leftHandSideExpression :  newExpression | callExpression ;

callExpression :  memberExpression arguments | callExpression arguments | callExpression [  ] | callExpression . identifierName

newExpression :  memberExpression | new newExpression

memberExpression :  primaryExpression | functionExpression | memberExpression [  ] | memberExpression . identifierName | new memberExpression arguments

functionExpression :  function identifier ( formalParameterList ) { functionBody } | function identifier ( ) { functionBody } | function ( formalParameterList ) { functionBody } | function ( ) { functionBody }

primaryExpression :  this | identifier | literal | arrayLiteral | objectLiteral | arguments

assignmentOperator : *= | /= | %= | += | -= | <<= | >>= | >>>= | &= | ^= | #=

literal : NullLiteral | BooleanLiteral | StringLiteral | RegularExpressionLiteral | numericLiteral

identifierName : identifier | reservedWord

reservedWord : keyword | futureReservedWord | NullLiteral | BooleanLiteral

keyword : break | do | instanceof | typeof | case | else | new | var | catch | finally | return | void | continue | for | switch | while | debugger | function | this | with | default | if | throw | delete | in | try | get | set 

futureReservedWord : class | enum | extends | super | const | export | import | implements | let | private | public | interface | package | protected | static | yield

NullLiteral : null

BooleanLiteral : true | false

numericLiteral : DecimalLiteral | HexIntegerLiteral | OctalIntegerLiteral | BinaryLiteral

StringLiteral :

RegularExpressionLiteral: 