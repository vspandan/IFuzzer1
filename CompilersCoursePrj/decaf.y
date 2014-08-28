%token INT BOOLEAN IF ELSE FOR RETURN BREAK CONTINUE CLASS VOID CALLOUT TRUE FALSE

%token ASSIGN_OP ID STRING_LITERAL ARITH_OP  REL_OP  EQ_OP  COND_OP INT_LITERAL

%%
program : CLASS PROGRAM '{' field_decl method_decl '}';

field_decl : type  field_block ',' ';' 
           |  ;

field_block : ID  | ID  '[' int_literal  ']'
            | ID  | ID  '[' int_literal  ']' field_block ;

method_decl  : type_decl ID  '(' args_decl ')' block
             |  ;

type_decl : type  
          | VOID ;

args_decl : TYPE ID
          | TYPE ID ',' args_decl ; 

block  : '{' var_decl* statement* '}';

var_decl :  TYPE ID+ ',' ';' ;

type : INT 
     | BOOLEAN ;

statement  : location ASSIGN_OP expr ';' 
         | method_call ';' 
         | IF ( expr  ) block  [ else block  ] 
         | FOR ID  = expr , expr  block 
         | RETURN [expr ] ';' 
         | BREAK ';'
         | CONTINUE ';' 
         | block ;

method_call  : method_name  ( [expr+,])
         | CALLOUT ( STRING_LITERAL  [, callout_arg+,]) ;

method_name : ID ;

location : ID 
         | ID  '[' expr  ']' ;

expr  : location
      | method_call
      | literal 
      | expr  bin_op expr 
      | - expr 
      | ! expr 
      | ( expr  );

callout_arg  : expr  
             | STRING_LITERAL ;

bin_op  : ARITH_OP  
        | REL_OP  
        | EQ_OP  
        | COND_OP ; 

bool_literal : TRUE 
             | FALSE;

//TODO LITERAL(should complete)
literal  : INT_LITERAL  
         | CHAR_LITERAL  
         | BOOL_LITERAL ;


ARITH_OP  : + | - | * | / | %
REL_OP  : < | > | <= |>=
EQ_OP  : == | !=
COND_OP  :  && | ||
CHAR_LITERAL :  'CHAR'
STRING_LITERAL : "CHAR*"



%%
