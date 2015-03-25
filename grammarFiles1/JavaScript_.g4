program : sourceElements | 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement

block : '{' statementList '}' |  '{' '}' 

statementList : statement | statement statementList

variableStatement : Var variableDeclarationList ';'

variableDeclarationList : variableDeclaration ',' variableDeclarationList | variableDeclaration

variableDeclaration : identifier initialiser |  identifier

initialiser : '=' singleExpression

emptyStatement : ';'

expressionStatement : expressionSequence

ifStatement : If '(' expressionSequence ')' statement Else statement | If '(' expressionSequence ')' statement 

iterationStatement : Do statement While '(' expressionSequence ')' ';' | While '(' expressionSequence ')' statement | For '(' ';' ';' ')' statement | For '(' ';' ';' expressionSequence ')' statement | For '(' ';' expressionSequence ';' ')' statement | For '(' ';' expressionSequence ';' expressionSequence ')' statement | For '(' expressionSequence ';' ';' ')' statement | For '(' expressionSequence ';' ';' expressionSequence ')' statement | For '(' expressionSequence ';' expressionSequence ';' ')' statement | For '(' expressionSequence ';' expressionSequence ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';' ';' ')' statement | For '(' Var variableDeclarationList ';' ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';' ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';' expressionSequence ')' statement | For '(' singleExpression In expressionSequence ')' statement | For '(' Var variableDeclaration In expressionSequence ')' statement

continueStatement : Continue identifier ';' | Continue ';'

breakStatement : Break identifier ';' | Break ';'

returnStatement : Return expressionSequence ';' | Return ';'

withStatement : With '(' expressionSequence ')' statement

switchStatement : Switch '(' expressionSequence ')' caseBlock

caseBlock : '{' caseClauses defaultClause caseClauses '}' | '{' caseClauses defaultClause '}' | '{' caseClauses '}' | '{' defaultClause caseClauses '}' |{' defaultClause '}' | '{' '}' 

caseClauses : caseClause | caseClause caseClauses

caseClause : Case expressionSequence ':' statementList |  Case expressionSequence ':'

defaultClause : Default ':' statementList | Default ':' 

labelledStatement : identifier ':' statement

throwStatement : Throw expressionSequence ';'

tryStatement : Try block catchProduction | Try block finallyProduction | Try block catchProduction finallyProduction

catchProduction : Catch '(' identifier ')' block

finallyProduction : Finally block

debuggerStatement : Debugger ';'

functionDeclaration : Function identifier '(' formalParameterList ')' '{' functionBody '}' | Function identifier '(' ')' '{' functionBody '}'

formalParameterList : identifier ',' formalParameterList| identifier

functionExpression	: Function '(' formalParameterList ')' '{' functionBody '}'	| Function  '(' ')' '{' functionBody '}'

functionBody : sourceElements |
    
arrayLiteral : '[' elementList ',' elision ']' | '[' elementList ',' ']' |'[' elementList ']' | '[' ',' elision ']' | '[' ',' ']' |'[' elision ']' | '['']'
 
elementList : elision singleExpression elementList | elision singleExpression | singleExpression |elision elementList

elision : ',' | ',' elision

objectLiteral : '{' '}' | '{' propertyNameAndValueList '}' |'{' propertyNameAndValueList ','  '}'

propertyNameAndValueList : propertyAssignment ',' propertyNameAndValueList | propertyAssignment
    
propertyAssignment : propertyName ':' singleExpression | 'get' identifier '(' ')' '{' functionBody '}'| 'set' identifier '(' propertySetParameterList ')' '{' functionBody '}'
    
propertyName : identifierName | StringLiteral | numericLiteral
    
propertySetParameterList : identifier

arguments : '(' argumentList ')' |  '(' ')'
    
argumentList : singleExpression ',' argumentList | singleExpression 
    
expressionSequence : singleExpression expressionSequence | singleExpression

singleExpression : functionExpression | singleExpression '[' expressionSequence ']' | singleExpression '.' identifierName | singleExpression arguments | New singleExpression arguments | New singleExpression | singleExpression '++' | singleExpression '--' | Delete singleExpression | Void singleExpression | Typeof singleExpression | '++' singleExpression | '--' singleExpression | '+' singleExpression | '-' singleExpression | '~' singleExpression | '!' singleExpression | singleExpression '*' singleExpression | singleExpression '/' singleExpression | singleExpression '%' singleExpression | singleExpression '+' singleExpression | singleExpression '-' singleExpression | singleExpression '<<' singleExpression | singleExpression '>>' singleExpression | singleExpression '>>>' singleExpression | singleExpression '<' singleExpression | singleExpression '>' singleExpression | singleExpression '<=' singleExpression | singleExpression '>=' singleExpression | singleExpression Instanceof singleExpression | singleExpression In singleExpression | singleExpression '==' singleExpression | singleExpression '!=' singleExpression | singleExpression '===' singleExpression | singleExpression '!==' singleExpression | singleExpression '&' singleExpression | singleExpression '^' singleExpression | singleExpression '|' singleExpression | singleExpression '&&' singleExpression | singleExpression '##' singleExpression | singleExpression '?' singleExpression ':' singleExpression | singleExpression '=' expressionSequence | singleExpression assignmentOperator expressionSequence | This | identifier | literal | arrayLiteral | objectLiteral | '(' expressionSequence ')'

assignmentOperator : '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|='

literal : nullLiteral | booleanLiteral | StringLiteral | RegularExpressionLiteral | numericLiteral

numericLiteral : DecimalLiteral | HexIntegerLiteral | OctalIntegerLiteral

identifierName : identifier | reservedWord

reservedWord : keyword | futureReservedWord | nullLiteral | booleanLiteral

keyword : Break | Do | Instanceof | Typeof | Case | Else | New | Var | Catch | Finally | Return | Void | Continue | For | Switch | While | Debugger | Function | This | With | Default | If | Throw | Delete | In | Try

futureReservedWord : Class | Enum | Extends | Super | Const | Export | Import | Implements | Let | Private | Public | Interface | Package | Protected | Static | Yield

nullLiteral : 'null'

booleanLiteral : 'true' | 'false'

Break      : 'break'
Do         : 'do'
Instanceof : 'instanceof'
Typeof     : 'typeof'
Case       : 'case'
Else       : 'else'
New        : 'new'
Var        : 'var'
Catch      : 'catch'
Finally    : 'finally'
Return     : 'return'
Void       : 'void'
Continue   : 'continue'
For        : 'for'
Switch     : 'switch'
While      : 'while'
Debugger   : 'debugger'
Function   : 'function'
This       : 'this'
With       : 'with'
Default    : 'default'
If         : 'if'
Throw      : 'throw'
Delete     : 'delete'
In         : 'in'
Try        : 'try'

Class   : 'class'
Enum    : 'enum'
Extends : 'extends'
Super   : 'super'
Const   : 'const'
Export  : 'export'
Import  : 'import'
Implements : 'implements'
Let        : 'let'
Private    : 'private'
Public     : 'public'
Interface  : 'interface'
Package    : 'package'
Protected  : 'protected'
Static     : 'static'
Yield      : 'yield'

identifier : Ident

