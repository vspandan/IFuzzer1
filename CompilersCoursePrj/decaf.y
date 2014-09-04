%token INT BOOLEAN IF ELSE FOR RETURN BREAK CONTINUE CLASS VOID CALLOUT TRUE FALSE

%token ASSIGN_OP ID STRING_LITERAL ARITH_OP  REL_OP  EQ_OP  COND_OP INT_LITERAL

%left '-' '!' ARITH_OP REL_OP EQ_OP COND_OP

%error-verbose

%%

program : CLASS ID '{' field_decl method_decl '}'
	
field_decl : type  fields ';' 
	   ;

fields  : field_block 
	| field_block ',' field_block ;

field_block : ID  
            | ID  '[' INT_LITERAL  ']' ;


method_decl  : type_decl ID  '(' args_decl ')' block 
	     | ;

type_decl : type 
          | VOID ;

args_decl : type ID
          | type ID ',' args_decl ; 

block  : '{' '}' 
       | '{' statement '}';

type : INT 
     | BOOLEAN ;

statement  : location ASSIGN_OP expr ';' 
         | method_call ';' 
         | IF '(' expr  ')' block  ELSE block
	 | IF '(' expr  ')' block  
         | FOR ID  '=' expr ',' expr  block 
         | RETURN [expr ] ';' 
         | BREAK ';'
         | CONTINUE ';' 
         | block ;

method_call  : method_name  '('  ')'
         | CALLOUT '(' STRING_LITERAL ',' callout_arg ')' ;
	 | CALLOUT '(' STRING_LITERAL  ')' ;

method_name : ID ;

location : ID 
         | ID  '[' expr  ']' ;

expr  : expr ARITH_OP term1
      | term1 ;

term1 : term1 REL_OP term2
      | term2 ;


term2 : term2 EQ_OP term3
      | term3 ;


term3 : term3 COND_OP term4 
      | term4 ;

term4 : location
      | method_call
      | literal 
      | '-' term4 
      | '!' term4 
      | '(' expr  ')' ;

callout_arg  : expr  
             | STRING_LITERAL ;

bool_literal : TRUE 
             | FALSE;

literal  : INT_LITERAL  
//         | CHAR_LITERAL  
         | bool_literal ;

%%

main()
{
	yyparse();
}


