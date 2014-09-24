
Program : SourceElements | 

SourceElements : SourceElement | SourceElements SourceElement

SourceElement : Statement | FunctionDeclaration

Statement : Block | VariableStatement | EmptyStatement | IfStatement | IterationStatement | ContinueStatement | BreakStatement | ReturnStatement | WithStatement | LabelledStatement | SwitchStatement | ThrowStatement | TryStatement | DebuggerStatement

Block : '{' StatementList '}'| EmptyBlock

EmptyBlock : '{' '}' 

StatementList : Statement | StatementList Statement

VariableStatement : Var VariableDeclarationList ';'

VariableDeclarationList : VariableDeclarationList  ',' VariableDeclaration | VariableDeclaration

VariableDeclaration : Identifier  | Identifier Initialiser 

Initialiser : '=' AssignmentExpression

EmptyStatement : ';'

IfStatement :  If '(' Expression ')' Statement 

IterationStatement : Do Statement While '(' Expression ')' ';' | While '(' Expression ')' Statement  | For '(' Expression ';' Expression ';' Expression ')' Statement | For '(' ';' Expression ';' Expression ')' Statement | For '(' Expression ';'  ';' Expression ')' Statement | For '(' ';' ';' Expression ')' Statement  | For '(' Expression ';' Expression ';'  ')' Statement | For '(' Expression ';'  ';'  ')' Statement | For '('  ';' Expression ';'  ')' Statement | For '(' ';' ';'  ')' Statement | For '(' Var VariableDeclarationList ';' Expression ';' Expression ')' Statement | For '(' Var VariableDeclarationList ';' Expression ';'  ')' Statement | For '(' Var VariableDeclarationList ';' ';' Expression ')' Statement | For '(' Var VariableDeclarationList ';'  ';'  ')' Statement | For '(' LeftHandSideExpression In Expression ')' Statement | For '(' Var VariableDeclaration In Expression ')' Statement

ContinueStatement : Continue Identifier ';' | Continue ';'

BreakStatement : Break Identifier ';' | Break ';'

ReturnStatement : Return Expression ';' | Return ';'

WithStatement : With '(' Expression ')' Statement

SwitchStatement : Switch '(' Expression ')' CaseBlock

CaseBlock : '{' CaseClauses  DefaultClause CaseClauses  '}' | '{' CaseClauses DefaultClause '}' | '{' CaseClauses '}' | '{' DefaultClause CaseClauses '}' | '{' DefaultClause '}' | '{' '}'

CaseClauses : CaseClause | CaseClauses CaseClause

CaseClause : Case Expression ':' StatementList | Case Expression ':' 

DefaultClause : Default ':' StatementList | Default ':' 

LabelledStatement : Identifier ':' Statement

ThrowStatement : Throw Expression ';'

TryStatement : Try Block CatchProduction | Try Block FinallyProduction | Try Block CatchProduction FinallyProduction

CatchProduction : Catch '(' Identifier ')' Block

FinallyProduction : Finally Block

DebuggerStatement : Debugger ';'

FunctionDeclaration : Function Identifier '(' FormalParameterList ')' '{' FunctionBody '}' | Function Identifier '('  ')' '{' FunctionBody '}'

FunctionExpression : Function '(' FormalParameterList ')' '{' FunctionBody '}' | Function  '(' ')' '{' FunctionBody '}'

FormalParameterList : FormalParameterList ',' Identifier | Identifier

FunctionBody : SourceElements | 
    
ElementList : AssignmentExpression |  ElementList ',' AssignmentExpression

ObjectLiteral : '{' PropertyNameAndValueList  '}'  

PropertyNameAndValueList : PropertyNameAndValueList  ',' PropertyAssignment | PropertyAssignment

PropertyAssignment : Identifier ':' Expression 

    
Arguments : '(' ArgumentList ')' | '(' ')'
    
ArgumentList : ArgumentList ',' AssignmentExpression | AssignmentExpression

MemberExpression : PrimaryExpression | FunctionExpression | MemberExpression '[' Expression ']' | MemberExpression '.' Identifier | New MemberExpression Arguments 

PrimaryExpression : This | NullLiteral | BooleanLiteral | ArrayLiteral | ObjectLiteral | '(' Expression ')' | NumericLiteral | StringLiteral

ArrayLiteral : '[' Elision ']' | '[' ElementList ']' | '[' ElementList ',' Elision ']'

Elision : Elision ',' | 

AssignmentExpression : ConditionalExpression | LeftHandSideExpression '=' AssignmentExpression | LeftHandSideExpression AssignmentOperator AssignmentExpression 

LeftHandSideExpression : New NewExpression | CallExpression 

CallExpression : MemberExpression Arguments | CallExpression '.' Identifier

Expression : AssignmentExpression 

ConditionalExpression : LogicalORExpression '?' AssignmentExpression ':' AssignmentExpression | LogicalORExpression

LogicalORExpression : LogicalORExpression '##' LogicalANDExpression | LogicalANDExpression

LogicalANDExpression : LogicalANDExpression '&&' BitwiseORExpression | BitwiseORExpression

BitwiseORExpression :  BitwiseORExpression '#' BitwiseXORExpression | BitwiseXORExpression

BitwiseXORExpression : BitwiseXORExpression '^' BitwiseANDExpression | BitwiseANDExpression

BitwiseANDExpression : BitwiseANDExpression '&' EqualityExpression | EqualityExpression

EqualityExpression : EqualityExpression '==' RelationalExpression | EqualityExpression '!=' RelationalExpression | EqualityExpression '===' RelationalExpression | EqualityExpression '!==' RelationalExpression | RelationalExpression

RelationalExpression : RelationalExpression '<' ShiftExpression | RelationalExpression '>' ShiftExpression | RelationalExpression '<=' ShiftExpression | RelationalExpression '>=' ShiftExpression | RelationalExpression Instanceof ShiftExpression | ShiftExpression   

ShiftExpression : ShiftExpression '<<' AdditiveExpression | ShiftExpression '>>' AdditiveExpression | ShiftExpression '>>>' AdditiveExpression | AdditiveExpression

AdditiveExpression : AdditiveExpression '+' MultiplicativeExpression | AdditiveExpression '-' MultiplicativeExpression | MultiplicativeExpression

MultiplicativeExpression : MultiplicativeExpression '*' UnaryExpression | MultiplicativeExpression '/' UnaryExpression | MultiplicativeExpression '%' UnaryExpression | UnaryExpression
 
UnaryExpression : Delete UnaryExpression | Void UnaryExpression | Typeof UnaryExpression | '++' UnaryExpression | '--' UnaryExpression | '+' UnaryExpression | '-' UnaryExpression | '~' UnaryExpression | '!' UnaryExpression | LeftHandSideExpression
 
AssignmentOperator : '*='  | '/='  | '%='  | '+='  | '-='  | '<<='  | '>>='  | '>>>='  | '&='  | '^=' 


NumericLiteral : INT_LITERAL

StringLiteral : STRING_LITERAL

NullLiteral : null

BooleanLiteral : true | false

Identifier : ID
