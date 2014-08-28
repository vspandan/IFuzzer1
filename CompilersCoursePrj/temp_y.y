ASSIGN_OP  : =
         | +=
         | -=


ID  : ALPHA  | ALPHA_NUM *
ALPHA_NUM  : ALPHA  | DIGIT 
DIGIT  : 0|1|2|3|4|5|6|7|8|9
ALPHA  : A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_
HEX_DIGIT  : DIGIT |A|B|C|D|E|F|a|b|c|d|e
INT_LITERAL  : DECIMAL_LITERAL  | HEX_LITERAL 
DECIMAL_LITERAL  : DIGIT DIGIT *
HEX LITERAL : 0X HEX_DIGIT HEX_DIGIT *

