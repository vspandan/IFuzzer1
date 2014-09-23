Program : SourceElements | 

SourceElements : SourceElement | SourceElements SourceElement

SourceElement : Statement | FunctionDeclaration

Statement : Block | VariableStatement | EmptyStatement | IfStatement | IterationStatement | ContinueStatement | BreakStatement | ReturnStatement | WithStatement | LabelledStatement | SwitchStatement | ThrowStatement | TryStatement | DebuggerStatement

Block : '{' StatementList '}'| EmptyBlock

EmptyBlock : '{' '}' 

StatementList : Statement | StatementList Statement

VariableStatement : var VariableDeclarationList ';'

VariableDeclarationList : VariableDeclarationList  ',' VariableDeclaration | VariableDeclaration

VariableDeclaration : Identifier  | Identifier Initialiser 

Initialiser : '=' AssignmentExpression

EmptyStatement : ';'

IfStatement :  if '(' Expression ')' Statement 

IterationStatement : do Statement while '(' Expression ')' ';' | while '(' Expression ')' Statement  | for '(' Expression ';' Expression ';' Expression ')' Statement | for '(' ';' Expression ';' Expression ')' Statement | for '(' Expression ';'  ';' Expression ')' Statement | for '(' ';' ';' Expression ')' Statement  | for '(' Expression ';' Expression ';'  ')' Statement | for '(' Expression ';'  ';'  ')' Statement | for '('  ';' Expression ';'  ')' Statement | for '(' ';' ';'  ')' Statement | for '(' var VariableDeclarationList ';' Expression ';' Expression ')' Statement | for '(' var VariableDeclarationList ';' Expression ';'  ')' Statement | for '(' var VariableDeclarationList ';' ';' Expression ')' Statement | for '(' var VariableDeclarationList ';'  ';'  ')' Statement | for '(' LeftHandSideExpression in Expression ')' Statement | for '(' var VariableDeclaration in Expression ')' Statement

ContinueStatement : continue Identifier ';' | continue ';'

BreakStatement : break Identifier ';' | break ';'

ReturnStatement : return Expression ';' | return ';'

WithStatement : with '(' Expression ')' Statement

SwitchStatement : switch '(' Expression ')' CaseBlock

CaseBlock : '{' CaseClauses  DefaultClause CaseClauses  '}' | '{' CaseClauses DefaultClause '}' | '{' CaseClauses '}' | '{' DefaultClause CaseClauses '}' | '{' DefaultClause '}' | '{' '}'

CaseClauses : CaseClause | CaseClauses CaseClause

CaseClause : case Expression ':' StatementList | case Expression ':' 

DefaultClause : default ':' StatementList | default ':' 

LabelledStatement : Identifier ':' Statement

ThrowStatement : throw Expression ';'

TryStatement : try Block CatchProduction | try Block FinallyProduction | try Block CatchProduction FinallyProduction

CatchProduction : catch '(' Identifier ')' Block

FinallyProduction : finally block

DebuggerStatement : debugger ';'

FunctionDeclaration : function Identifier '(' FormalParameterList ')' '{' FunctionBody '}' | function Identifier '('  ')' '{' FunctionBody '}'

FunctionExpression : function '(' FormalParameterList ')' '{' FunctionBody '}' | function  '(' ')' '{' FunctionBody '}'

FormalParameterList : FormalParameterList ',' Identifier | Identifier

FunctionBody : SourceElements | 
    
ElementList : AssignmentExpression |  ElementList ',' AssignmentExpression

ObjectLiteral : '{' PropertyNameAndValueList  '}'  

PropertyNameAndValueList : PropertyNameAndValueList  ',' PropertyAssignment | PropertyAssignment

PropertyAssignment : Identifier ':' Expression 

    
Arguments : '(' ArgumentList ')' | '(' ')'
    
ArgumentList : ArgumentList ',' AssignmentExpression | AssignmentExpression

MemberExpression : PrimaryExpression | FunctionExpression | MemberExpression '[' Expression ']' | MemberExpression '.' Identifier | new MemberExpression Arguments 

PrimaryExpression : this | NullLiteral | BooleanLiteral | ArrayLiteral | ObjectLiteral | '(' Expression ')' | NumericLiteral | StringLiteral

ArrayLiteral : '[' Elision ']' | '[' ElementList ']' | '[' ElementList ',' Elision ']'

Elision : Elision ',' | 

AssignmentExpression : ConditionalExpression | LeftHandSideExpression '=' AssignmentExpression | LeftHandSideExpression AssignmentOperator AssignmentExpression 

LeftHandSideExpression : new NewExpression | CallExpression 

CallExpression : MemberExpression Arguments | CallExpression '.' Identifier

Expression : AssignmentExpression 

ConditionalExpression : LogicalORExpression '?' AssignmentExpression ':' AssignmentExpression | LogicalORExpression

LogicalORExpression : LogicalORExpression '##' LogicalANDExpression | LogicalANDExpression

LogicalANDExpression : LogicalANDExpression '&&' BitwiseORExpression | BitwiseORExpression

BitwiseORExpression :  BitwiseORExpression '#' BitwiseXORExpression | BitwiseXORExpression

BitwiseXORExpression : BitwiseXORExpression '^' BitwiseANDExpression | BitwiseANDExpression

BitwiseANDExpression : BitwiseANDExpression '&' EqualityExpression | EqualityExpression

EqualityExpression : EqualityExpression '==' RelationalExpression | EqualityExpression '!=' RelationalExpression | EqualityExpression '===' RelationalExpression | EqualityExpression '!==' RelationalExpression | RelationalExpression

RelationalExpression : RelationalExpression '<' ShiftExpression | RelationalExpression '>' ShiftExpression | RelationalExpression '<=' ShiftExpression | RelationalExpression '>=' ShiftExpression | RelationalExpression instanceof ShiftExpression | ShiftExpression   

ShiftExpression : ShiftExpression '<<' AdditiveExpression | ShiftExpression '>>' AdditiveExpression | ShiftExpression '>>>' AdditiveExpression | AdditiveExpression

AdditiveExpression : AdditiveExpression '+' MultiplicativeExpression | AdditiveExpression '-' MultiplicativeExpression | MultiplicativeExpression

MultiplicativeExpression : MultiplicativeExpression '*' UnaryExpression | MultiplicativeExpression '/' UnaryExpression | MultiplicativeExpression '%' UnaryExpression | UnaryExpression
 
UnaryExpression : delete UnaryExpression | void UnaryExpression | typeof UnaryExpression | '++' UnaryExpression | '--' UnaryExpression | '+' UnaryExpression | '-' UnaryExpression | '~' UnaryExpression | '!' UnaryExpression | LeftHandSideExpression
 
AssignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^=' 


NumericLiteral : INT_LITERAL

StringLiteral : STRING_LITERAL

NullLiteral : null

BooleanLiteral : true | false

Identifier : ID
