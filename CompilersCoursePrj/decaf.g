PROGRAM  : CLASS PROGRAM '{' FIELD_DECL * MEDHOD_DECL * '}'
FIELD_DECL : TYPE  { ID  | ID  '[' INT_LITERAL  ']' }+,;
METHOD_DECL  : { TYPE  | VOID } ID  ( [{TYPE  ID }+ ,]) BLOCK 
BLOCK  : '{' VAR_DECL * STATEMENT * '}'
VAR_DECL  : TYPE ID +,;
TYPE  : INT | BOOLEAN
STATEMENT  : LOCATION ASSIGN_OP EXPR ;
         | METHOD_CALL ;
         | IF ( EXPR  ) BLOCK  [ ELSE BLOCK  ]
         | FOR ID  = EXPR , EXPR  BLOCK 
         | RETURN [EXPR ] ;
         | BREAK ;
         | CONTINUE ;
         | BLOCK 
ASSIGN_OP  : =
         | +=
         | -=
METHOD_CALL  : METHOD_NAME  ( [EXPR +,])
         | CALLOUT ( STRING_LITERAL  [, CALLOUT_ARG +,])
MEDHOD_NAME  : ID 
LOCATION  : ID 
         | ID  '[' EXPR  ']'
EXPR  : LOCATION 
         | METHOD_CALL 
		 | LITERAL 
         | EXPR  BIN_OP EXPR 
         | - EXPR 
         | ! EXPR 
         | ( EXPR  )
CALLOUT_ARG  : EXPR  |STRING_LITERAL 
BIN_OP  : ARITH_OP  | REL_OP  | EQ_OP  | COND_OP 
ARITH_OP  : + | - | * | / | %
REL_OP  : < | > | <= |>=
EQ_OP  : == | !=
COND_OP  :  && | ||
LITERAL  : INT_LITERAL  | CHAR_LITERAL  | BOOL_LITERAL 
ID  : ALPHA  | ALPHA_NUM *
ALPHA_NUM  : ALPHA  | DIGIT 
DIGIT  : 0|1|2|3|4|5|6|7|8|9
ALPHA  : A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_
HEX_DIGIT  : DIGIT |A|B|C|D|E|F|a|b|c|d|e
INT_LITERAL  : DECIMAL_LITERAL  | HEX_LITERAL 
DECIMAL_LITERAL  : DIGIT DIGIT *
HEX LITERAL : 0X HEX_DIGIT HEX_DIGIT *
BOOL_LITERAL : TRUE | FALSE
CHAR_LITERAL :  'CHAR'
STRING_LITERAL : "CHAR*"

