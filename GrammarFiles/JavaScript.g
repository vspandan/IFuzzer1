program : sourceElements EOF | WhiteSpaces 

sourceElements : sourceElement | sourceElement sourceElements

sourceElement : statement | functionDeclaration

statement : block | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | debuggerStatement 

block : '{' statementList '}' | { }

statementList : statement | statement statementList 

variableStatement : Var variableDeclarationList eos

variableDeclarationList : variableDeclaration ( ',' variableDeclaration ) variableDeclarationList | variableDeclaration

variableDeclaration : Identifier initialiser | Identifier initialiser

initialiser : '=' singleExpression

emptyStatement : SemiColon

expressionStatement : expressionSequence

ifStatement : If '(' expressionSequence ')' statement ( Else statement ) | If '(' expressionSequence ')' statement

iterationStatement : Do statement While '(' expressionSequence ')' eos | While '(' expressionSequence ')' statement | For '(' expressionSequence ';' expressionSequence ';' expressionSequence ')' statement | For '(' ';' expressionSequence ';' expressionSequence ')' statement | For '(' expressionSequence ';'  ';' expressionSequence ')' statement | For '(' ';' ';' expressionSequence ')' statement | For '(' expressionSequence ';' expressionSequence ';'  ')' statement  | For '(' expressionSequence ';'  ';'  ')' statement | For '('  ';' expressionSequence ';'  ')' statement | For '(' ';' ';'  ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';' expressionSequence ';'  ')' statement | For '(' Var variableDeclarationList ';' ';' expressionSequence ')' statement | For '(' Var variableDeclarationList ';'  ';'  ')' statement | For '(' singleExpression In expressionSequence ')' statement | For '(' Var variableDeclaration In expressionSequence ')' statement

continueStatement : Continue Identifier eos | Continue  eos

breakStatement : Break Identifier eos | Break eos

returnStatement : Return expressionSequence eos | Return eos
 
withStatement : With '(' expressionSequence ')' statement

switchStatement : Switch '(' expressionSequence ')' caseBlock

caseBlock : '{' caseClauses ( defaultClause caseClauses ) '}' | '{' caseClauses ( defaultClause ) '}' | '{' caseClauses '}' | '{' ( defaultClause caseClauses ) '}' | '{' ( defaultClause ) '}' | '{' '}'

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

elementList : elision singleExpression ( ',' elision singleExpression ) elementList | elision singleExpression | elision singleExpression ( ',' singleExpression ) elementList |  singleExpression ( ',' elision singleExpression ) elementList |  singleExpression ( ',' singleExpression ) elementList |  elision singleExpression |  singleExpression |  singleExpression

elision : ','+ 

objectLiteral : '{' propertyNameAndValueList ',' '}' | '{' propertyNameAndValueList  '}' | '{'  ',' '}' | '{'   '}'

