program : sourceElements | 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement

block : '{' statementList '}' 

statementList : statement | statement statementList | 

variableStatement : Var variableDeclarationList eos

variableDeclarationList : variableDeclaration ',' variableDeclarationList | variableDeclaration

variableDeclaration : Identifier  | Identifier initialiser | 

initialiser : '=' singleExpression

emptyStatement : ';'

expressionStatement : expressionSequence

ifStatement : If '(' expressionSequence ')' statement Else statement  | If '(' expressionSequence ')' statement 

iterationStatement : Do statement While '(' expressionSequence ')' eos | While '(' expressionSequence ')' statement  | For '(' expressionSequence ';' expressionSequence ';' expressionSequence ')' statement | For '(' ';' expressionSequence ';' expressionSequence ')' statement | For '(' expressionSequence ';'  ';' expressionSequence ')' statement | For '(' ';' ';' expressionSequence ')' statement  | For '(' expressionSequence ';' expressionSequence ';'  ')' statement | For '(' expressionSequence ';'  ';'  ')' statement | For '('  ';' expressionSequence ';'  ')' statement | For '(' ';' ';'  ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';'  ')' statement | For '(' Var variableDeclarationList ';' ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';'  ';'  ')' statement | For '(' singleExpression In expressionSequence ')' statement | For '(' Var variableDeclaration In expressionSequence ')' statement

continueStatement : Continue Identifier eos | Continue eos

breakStatement : Break Identifier eos | Break eos

returnStatement : Return expressionSequence eos | Return eos

withStatement : With '(' expressionSequence ')' statement

switchStatement : Switch '(' expressionSequence ')' caseBlock

caseBlock : '{' caseClauses  defaultClause caseClauses  '}' | '{' caseClauses defaultClause '}' | '{' caseClauses '}' | '{' defaultClause caseClauses '}' | '{' defaultClause '}' | '{' '}'

caseClauses : caseClause | caseClause caseClauses

caseClause : Case expressionSequence ':' statementList | Case expressionSequence ':' 

defaultClause : Default ':' statementList | Default ':' 

labelledStatement : Identifier ':' statement

throwStatement : Throw expressionSequence eos

tryStatement : Try block catchProduction | Try block finallyProduction | Try block catchProduction finallyProduction

catchProduction : Catch '(' Identifier ')' block

finallyProduction : Finally block

debuggerStatement : Debugger eos

functionDeclaration : Function Identifier '(' formalParameterList ')' '{' functionBody '}' | Function Identifier '('  ')' '{' functionBody '}'

formalParameterList : Identifier ',' formalParameterList | Identifier

functionBody : sourceElements | 
    
arrayLiteral : '[' ']' | '[' elementList  ']' | '[' elementList ',' elision ']'

elementList :  elisionExpr elementList | elisionExpr

elisionExprs : elisionExpr ',' elisionExprs | elisionExpr 

elisionExpr : elision singleExpression  

elision : ',' | elision ',' | 

objectLiteral : '{' propertyNameAndValueList ',' '}' | '{' propertyNameAndValueList  '}' | '{'  ',' '}' | '{'   '}'

propertyNameAndValueList : propertyAssignments propertyNameAndValueList | propertyAssignment

propertyAssignments : propertyAssignment ',' propertyAssignments 
    
propertyAssignment : propertyName ':' singleExpression | Identifier '(' ')' '{' functionBody '}' | Identifier '(' propertySetParameterList ')' '{' functionBody '}'

propertyName : identifierName | StringLiteral | numericLiteral
    
propertySetParameterList : Identifier

arguments : '(' argumentList ')' | '(' ')'
    
argumentList : singleExpressions argumentList | singleExpression

singleExpressions : singleExpression ',' singleExpressions
    
expressionSequence : singleExpressions expressionSequence | singleExpression

singleExpression : singleExpression '[' expressionSequence ']' | singleExpression '.' identifierName | singleExpression arguments | New singleExpression arguments | New singleExpression | singleExpression '++' | singleExpression  '--' | Delete singleExpression | Void singleExpression | Typeof singleExpression | '++' literal | '--' literal | '+' literal | '-' literal | '~' singleExpression | '!' singleExpression | literal '*' literal | literal '/' literal | literal '%' literal | literal '+' literal | literal '-' literal | literal '<<' literal | literal '>>' literal | literal '>>>' literal | literal '<' literal | literal '>' literal | literal '<=' literal | literal '>=' literal | singleExpression Instanceof singleExpression | singleExpression In singleExpression | literal '==' literal | literal '!=' literal | literal '===' literal | literal '!==' literal | literal '&' literal | literal '^' literal |  literal '&&' literal | singleExpression '?' singleExpression ':' singleExpression | singleExpression '=' expressionSequence | singleExpression assignmentOperator expressionSequence | This | Identifier | literal | arrayLiteral | objectLiteral                                                          
 | '(' expressionSequence ')'
 
assignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^=' 

identifierName : Identifier | reservedWord

keyword : Break | Do | Instanceof | Typeof | Case | Else | New | Var | Catch | Finally | Return | Void | Continue | For | Switch | While | Debugger | Function | This | With | Default | If | Throw | Delete | In | Try

reservedWord : keyword | futureReservedWord | NullLiteral | BooleanLiteral

literal : NullLiteral | BooleanLiteral | numericLiteral | StringLiteral 

numericLiteral : INT_LITERAL

StringLiteral : STRING_LITERAL

NullLiteral : null

BooleanLiteral : true | false

futureReservedWord : Class | Enum | Extends | Super | Const | Export | Import | Implements | Let | Private | Public | Interface | Package | Protected | Static | Yield

eos : SemiColon | 

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

Identifier : ID