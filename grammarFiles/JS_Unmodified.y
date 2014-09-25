Program : SourceElements | 

SourceElements : SourceElement | SourceElements SourceElement

SourceElement : Statement | FunctionDeclaration

PrimaryExpression : this | Identifier | Literal | ArrayLiteral | ObjectLiteral | '(' Expression ')'

ArrayLiteral : '[' Elision ']' | '[' ElementList ']' | '[' ElementList ',' Elision ']'

Elision : Elision ',' | 

ElementList : Elision AssignmentExpression |  ElementList ',' Elision AssignmentExpression

ObjectLiteral : '{' PropertyNameAndValueList  '}' |  '{' PropertyNameAndValueList  ',' '}' 

PropertyNameAndValueList : PropertyNameAndValueList  ',' PropertyAssignment | PropertyAssignment

PropertyAssignment : PropertyName ':' AssignmentExpression | 'get'PropertyName '(' ')' '{' FunctionBody '}' | 'set'PropertyName '(' Identifier ')' '{' FunctionBody '}'

PropertyName : Identifier | NumericLiteral | StringLiteral

MemberExpression : PrimaryExpression | FunctionExpression | MemberExpression '[' Expression ']' | MemberExpression '.' Identifier | new MemberExpression Arguments

NewExpression : new NewExpression | MemberExpression

CallExpression : MemberExpression Arguments | CallExpression Arguments | CallExpression '[' Expression ']' | CallExpression '.' Identifier

Arguments : '(' ArgumentList ')' | '(' ')'
    
ArgumentList : ArgumentList ',' AssignmentExpression | AssignmentExpression

LeftHandSideExpression : NewExpression | CallExpression 

UnaryExpression : delete UnaryExpression | void UnaryExpression | typeof UnaryExpression | '++' UnaryExpression | '--' UnaryExpression | '+' UnaryExpression | '-' UnaryExpression | '~' UnaryExpression | '!' UnaryExpression | LeftHandSideExpression

MultiplicativeExpression : MultiplicativeExpression '*' UnaryExpression | MultiplicativeExpression '/' UnaryExpression | MultiplicativeExpression '%' UnaryExpression | UnaryExpression

AdditiveExpression : AdditiveExpression '+' MultiplicativeExpression | AdditiveExpression '-' MultiplicativeExpression | MultiplicativeExpression

ShiftExpression : ShiftExpression '<<' AdditiveExpression | ShiftExpression '>>' AdditiveExpression | ShiftExpression '>>>' AdditiveExpression | AdditiveExpression

RelationalExpression : RelationalExpression '<' ShiftExpression | RelationalExpression '>' ShiftExpression | RelationalExpression '<=' ShiftExpression | RelationalExpression '>=' ShiftExpression | RelationalExpression instanceof ShiftExpression | RelationalExpression in ShiftExpression | ShiftExpression

EqualityExpression : EqualityExpression '==' RelationalExpression | EqualityExpression '!=' RelationalExpression | EqualityExpression '===' RelationalExpression | EqualityExpression '!==' RelationalExpression | RelationalExpression

BitwiseANDExpression : BitwiseANDExpression '&' EqualityExpression | EqualityExpression

BitwiseXORExpression : BitwiseXORExpression '^' BitwiseANDExpression | BitwiseANDExpression

BitwiseORExpression :  BitwiseORExpression '#' BitwiseXORExpression | BitwiseXORExpression

LogicalANDExpression : LogicalANDExpression '&&' BitwiseORExpression | BitwiseORExpression   

LogicalORExpression : LogicalORExpression '##' LogicalANDExpression | LogicalANDExpression

ConditionalExpression : LogicalORExpression '?' AssignmentExpression ':' AssignmentExpression | LogicalORExpression

AssignmentExpression : ConditionalExpression | LeftHandSideExpression '=' AssignmentExpression | LeftHandSideExpression AssignmentOperator AssignmentExpression

AssignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^=' 

Expression : AssignmentExpression | AssignmentExpression ',' Expression

Statement : Block | VariableStatement | EmptyStatement | Expression | IfStatement | IterationStatement | ContinueStatement | BreakStatement | ReturnStatement | WithStatement | LabelledStatement | SwitchStatement | ThrowStatement | TryStatement | DebuggerStatement

Block : '{' StatementList '}'| EmptyBlock

EmptyBlock : '{' '}' 

StatementList : Statement | StatementList Statement

VariableStatement : var VariableDeclarationList ';'

VariableDeclarationList : VariableDeclarationList  ',' VariableDeclaration | VariableDeclaration

VariableDeclaration : Identifier  | Identifier Initialiser 

Initialiser : '=' AssignmentExpression

EmptyStatement : ';'

IfStatement :  if '(' Expression ')' Statement else Statement | if '(' Expression ')' Statement   

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






    