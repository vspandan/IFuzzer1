program : sourceElements | WhiteSpaces |

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement

block : '{' statementList '}' 

statementList : statement | statement statementList | 

variableStatement : var variableDeclarationList eos

variableDeclarationList : variableDeclaration ',' variableDeclarationList | variableDeclaration

variableDeclaration : Identifier  | Identifier initialiser

initialiser : '=' singleExpression

emptyStatement : ';'

expressionStatement : expressionSequence

ifStatement : If '(' expressionSequence ')' statement Else statement  | If '(' expressionSequence ')' statement 

iterationStatement
 : Do statement While '(' expressionSequence ')' eos | While '(' expressionSequence ')' statement  | For '(' expressionSequence ';' expressionSequence ';' expressionSequence ')' statement | For '(' ';' expressionSequence ';' expressionSequence ')' statement | For '(' expressionSequence ';'  ';' expressionSequence ')' statement | For '(' ';' ';' expressionSequence ')' statement  | For '(' expressionSequence ';' expressionSequence ';'  ')' statement | For '(' expressionSequence ';'  ';'  ')' statement | For '('  ';' expressionSequence ';'  ')' statement | For '(' ';' ';'  ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';'  ')' statement | For '(' Var variableDeclarationList ';' ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';'  ';'  ')' statement | For '(' singleExpression In expressionSequence ')' statement | For '(' Var variableDeclaration In expressionSequence ')' statement

continueStatement : Continue Identifier eos | Continue eos

breakStatement : Break Identifier eos | Break eos

returnStatement : Return expressionSequence eos | Return eos

withStatement : With '(' expressionSequence ')' statement

switchStatement : Switch '(' expressionSequence ')' caseBlock

caseBlock : '{' caseClauses  defaultClause caseClauses  '}' | '{' caseClauses ( defaultClause ) '}' | '{' caseClauses '}' | '{' ( defaultClause caseClauses ) '}' | '{' ( defaultClause ) '}' | '{' '}'

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

formalParameterList : Identifier ( ',' formalParameterList ) | Identifier

functionBody : sourceElements | ' '
    
arrayLiteral : '[' elementList ','? elision ']' | '[' ','? elision ']' | '[' elementList ','?  ']' | '[' ','?  ']'

elementList : elision singleExpression ( ',' elision singleExpression ) elementList | elision singleExpression  | elision singleExpression ( ',' singleExpression ) elementList | singleExpression ( ',' elision singleExpression ) elementList |  singleExpression ( ',' singleExpression ) elementList |  elision singleExpression  |  singleExpression  | singleExpression 

elision : ','+

objectLiteral : '{' propertyNameAndValueList ',' '}' | '{' propertyNameAndValueList  '}' | '{'  ',' '}' | '{'   '}'

propertyNameAndValueList : propertyAssignment ( ',' propertyAssignment ) propertyNameAndValueList | propertyAssignment 
    
propertyAssignment : propertyName ':' singleExpression | getter '(' ')' '{' functionBody '}' | setter '(' propertySetParameterList ')' '{' functionBody '}'

propertyName : identifierName | StringLiteral | numericLiteral
    
propertySetParameterList : Identifier

arguments : '(' argumentList ')' | '(' ')'
    
argumentList : singleExpression ( ',' singleExpression ) argumentList | singleExpression
    
expressionSequence : singleExpression ( ',' singleExpression ) expressionSequence | singleExpression

singleExpression : singleExpression '[' expressionSequence ']' | singleExpression '.' identifierName | singleExpression arguments | New singleExpression arguments | New singleExpression | singleExpression {!here(LineTerminator)} '++' | singleExpression '++' | singleExpression {!here(LineTerminator)} '--' | singleExpression  '--' | Delete singleExpression | Void singleExpression | Typeof singleExpression | '++' literal | '--' literal | '+' literal | '-' literal | '~' singleExpression | '!' singleExpression | literal '*' literal | literal '/' literal | literal '%' literal | literal '+' literal | literal '-' literal | literal '<<' literal | literal '>>' literal | literal '>>>' literal | literal '<' literal | literal '>' literal | literal '<=' literal | literal '>=' literal | singleExpression Instanceof singleExpression | singleExpression In singleExpression | literal '==' literal | literal '!=' literal | literal '===' literal | literal '!==' literal | literal '&' literal | literal '^' literal | literal '|' literal | literal '&&' literal | literal '||' literal | singleExpression '?' singleExpression ':' singleExpression | singleExpression '=' expressionSequence | singleExpression assignmentOperator expressionSequence | This | Identifier | literal | arrayLiteral | objectLiteral                                                          
 | '(' expressionSequence ')' 

assignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^='  | '|=' 

eos : SemiColon | EOF | ' '


OpenBracket                : '['
CloseBracket               : ']'
OpenParen                  : '('
CloseParen                 : ')'
OpenBrace                  : '{'
CloseBrace                 : '}'
SemiColon                  : ';'
Comma                      : ','
Assign                     : '='
QuestionMark               : '?'
Colon                      : ':'
Dot                        : '.'
PlusPlus                   : '++'
MinusMinus                 : '--'
Plus                       : '+'
Minus                      : '-'
BitNot                     : '~'
Not                        : '!'
Multiply                   : '*'
Divide                     : '/'
Modulus                    : '%'
RightShiftArithmetic       : '>>
LeftShiftArithmetic        : '<<
RightShiftLogical          : '>>>'
LessThan                   : '<'
MoreThan                   : '>'
LessThanEquals             : '<='
GreaterThanEquals          : '>='
Equals                     : '=='
NotEquals                  : '!='
IdentityEquals             : '==='
IdentityNotEquals          : '!=='
BitAnd                     : '&'
BitXOr                     : '^'
BitOr                      : '|'
And                        : '&&'
Or                         : '||'
MultiplyAssign             : '*='
DivideAssign               : '/=' 
ModulusAssign              : '%=' 
PlusAssign                 : '+=' 
MinusAssign                : '-=' 
LeftShiftArithmeticAssign  : '<<=' 
RightShiftArithmeticAssign : '>>=' 
RightShiftLogicalAssign    : '>>>=' 
BitAndAssign               : '&=' 
BitXorAssign               : '^=' 
BitOrAssign                : '|='

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




UnexpectedCharacter : .
