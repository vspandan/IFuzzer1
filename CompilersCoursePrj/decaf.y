%token INT BOOLEAN IF ELSE FOR RETURN BREAK CONTINUE CLASS VOID CALLOUT TRUE FALSE

%token ASSIGN_OP ID STRING_LITERAL ARITH_OP  REL_OP  EQ_OP  COND_OP INT_LITERAL E_ASSIGN_OP MINUS

%left '-' '!' ARITH_OP REL_OP EQ_OP COND_OP

%error-verbose

%%

program : CLASS ID '{' field_decl method_decl '}'
	| CLASS ID '{' method_decl '}' ;

//field_decls : field_decl  
//	    | field_decl field_decls ;
	
field_decl : type  fields ':' ;

fields  : field_block 
	| field_block ',' fields ;

field_block : ID  
            | ID  '[' INT_LITERAL  ']' ;

//method_decls : method_decl
//	       | method_decl method_decls ;

method_decl  : type ID  '(' args_decl ')' block 
	     | VOID ID  '(' args_decl ')' block 
	     | ;	

args_decl : type ID
          | type ID ',' args_decl ;
 
vars : ID ';'
     | ID ',' vars;

var_decl : type vars var_decl
	 | type vars
	 ;

block  : '{' block_body '}' 
       ;

statements : statement
	   | statement statements

block_body : var_decl statements
	   | var_decl
	   | statements 
	   | ;

type : INT 
     | BOOLEAN ;

statement: location ASSGN_OP expr ';' 
	 | method_call ';' 
         | IF '(' expr  ')' block  ELSE block
	 | IF '(' expr  ')' block  
         | FOR ID  E_ASSIGN_OP expr ',' expr  block 
         | RETURN ';'
	 | RETURN expr ';' 
         | BREAK ';'
         | CONTINUE ';' 
         | block ;

ASSGN_OP : ASSIGN_OP
	 | E_ASSIGN_OP ;
	 
exprs : expr
	| expr ',' exprs ;

callout_args : callout_arg
             | callout_arg ',' callout_args ;

method_call  : method_name '('   ')'
	 | method_name '(' exprs ')'
         | CALLOUT '(' STRING_LITERAL ',' callout_args ')' 
	 | CALLOUT '(' STRING_LITERAL  ')' ;

method_name : ID ;

location : ID 
         | ID  '[' expr  ']' ;

ARTH_OP : ARITH_OP 
	| MINUS ;

expr  : expr ARTH_OP term1
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
      | MINUS term4 
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


