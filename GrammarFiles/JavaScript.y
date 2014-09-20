program : sourceElements | 

sourceElements : sourceElement | sourceElements sourceElement

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expression | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement

block : '{' statementList '}'| empty

empty : '{' '}' 

statementList : statement | statementList statement

variableStatement : var variableDeclarationList ';'

variableDeclarationList : variableDeclarationList  ',' variableDeclaration | variableDeclaration

variableDeclaration : Identifier  | Identifier initialiser 

initialiser : '=' assignmentExpression

emptyStatement : ';'

ifStatement : if '(' expression ')' statement else statement | if '(' expression ')' statement   

iterationStatement : do statement while '(' expression ')' ';' | while '(' expression ')' statement  | for '(' expression ';' expression ';' expression ')' statement | for '(' ';' expression ';' expression ')' statement | for '(' expression ';'  ';' expression ')' statement | for '(' ';' ';' expression ')' statement  | for '(' expression ';' expression ';'  ')' statement | for '(' expression ';'  ';'  ')' statement | for '('  ';' expression ';'  ')' statement | for '(' ';' ';'  ')' statement | for '(' var variableDeclarationList ';' expression ';' expression ')' statement | for '(' var variableDeclarationList ';' expression ';'  ')' statement | for '(' var variableDeclarationList ';' ';' expression ')' statement | for '(' var variableDeclarationList ';'  ';'  ')' statement | for '(' leftHandSideExpression in expression ')' statement | for '(' var variableDeclaration in expression ')' statement

continueStatement : continue Identifier ';' | continue ';'

breakStatement : break Identifier ';' | break ';'

returnStatement : return expression ';' | return ';'

withStatement : with '(' expression ')' statement

switchStatement : switch '(' expression ')' caseBlock

caseBlock : '{' caseClauses  defaultClause caseClauses  '}' | '{' caseClauses defaultClause '}' | '{' caseClauses '}' | '{' defaultClause caseClauses '}' | '{' defaultClause '}' | '{' '}'

caseClauses : caseClause | caseClauses caseClause

caseClause : case expression ':' statementList | case expression ':' 

defaultClause : default ':' statementList | default ':' 

labelledStatement : Identifier ':' statement

throwStatement : throw expression ';'

tryStatement : try block catchProduction | try block finallyProduction | try block catchProduction finallyProduction

catchProduction : catch '(' Identifier ')' block

finallyProduction : finally block

debuggerStatement : debugger ';'

functionDeclaration : function Identifier '(' formalParameterList ')' '{' functionBody '}' | function Identifier '('  ')' '{' functionBody '}'

functionExpression : function '(' formalParameterList ')' '{' functionBody '}' | function  '(' ')' '{' functionBody '}'

formalParameterList : formalParameterList ',' Identifier | Identifier

functionBody : sourceElements | 
    
elementList : assignmentExpression |  elementList ',' assignmentExpression

objectLiteral : '{' propertyNameAndValueList  '}'  

propertyNameAndValueList : propertyNameAndValueList  ',' propertyAssignment | propertyAssignment

propertyAssignment : propertyName ':' assignmentExpression | Identifier '(' ')' '{' functionBody '}' | Identifier '(' propertySetParameterList ')' '{' functionBody '}'

propertyName : StringLiteral | numericLiteral
    
propertySetParameterList : Identifier

arguments : '(' argumentList ')' | '(' ')'
    
argumentList : argumentList ',' assignmentExpression | assignmentExpression

memberExpression : primaryExpression | functionExpression | memberExpression '[' expression ']' | memberExpression '.' Identifier | new memberExpression Arguments 

primaryExpression : this | identifier | literal | arrayLiteral | objectLiteral | '(' expression ')'

arrayLiteral : '[' elision ']' | '[' elementList ']' | '[' elementList ',' elision ']'

elision : elision ',' | 

assignmentExpression : conditionalExpression | leftHandSideExpression '=' assignmentExpression | leftHandSideExpression assignmentOperator assignmentExpression 

leftHandSideExpression : newExpression | callExpression

callExpression : memberExpression arguments | callExpression arguments | callExpression '[' expression ']' | callExpression '.' Identifier

newExpression :  memberExpression | new newExpression

expression : assignmentExpression | expression ',' assignmentExpression

conditionalExpression : logicalORExpression | logicalORExpression '?' assignmentExpression ':' assignmentExpression

logicalORExpression : logicalANDExpression | logicalORExpression '##' logicalANDExpression

logicalANDExpression : bitwiseORExpression | logicalANDExpression '&&' bitwiseORExpression

bitwiseORExpression : bitwiseXORExpression | bitwiseORExpression '#' bitwiseXORExpression

bitwiseXORExpression : bitwiseANDExpression | bitwiseXORExpression '^' bitwiseANDExpression

bitwiseANDExpression : equalityExpression | bitwiseANDExpression '&' equalityExpression

equalityExpression : relationalExpression | equalityExpression '==' relationalExpression | equalityExpression '!=' relationalExpression | equalityExpression '===' relationalExpression | equalityExpression '!==' relationalExpression

relationalExpression : shiftExpression | relationalExpression '<' shiftExpression | relationalExpression '>' shiftExpression | relationalExpression '<=' shiftExpression | relationalExpression '>=' shiftExpression | relationalExpression instanceof shiftExpression

shiftExpression : additiveExpression | shiftExpression '<<' additiveExpression | shiftExpression '>>' additiveExpression | shiftExpression '>>>' additiveExpression

additiveExpression : multiplicativeExpression | additiveExpression '+' multiplicativeExpression | additiveExpression '-' multiplicativeExpression 

multiplicativeExpression : unaryExpression | multiplicativeExpression '*' unaryExpression | multiplicativeExpression '/' unaryExpression | multiplicativeExpression '%' unaryExpression
 
unaryExpression : delete unaryExpression | void UnaryExpression | typeof UnaryExpression | '++' unaryExpression | '--' unaryExpression | '+' UnaryExpression | '-' UnaryExpression | '~' UnaryExpression | '!' UnaryExpression
 
assignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^=' 

literal : NullLiteral | BooleanLiteral | numericLiteral | StringLiteral 

numericLiteral : INT_LITERAL

StringLiteral : STRING_LITERAL

NullLiteral : null

BooleanLiteral : true | false

Identifier : ID
