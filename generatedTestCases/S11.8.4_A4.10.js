if ( ( "x" >= "x " ) !== false ) { $ERROR ( '#1: ("x" >= "x ") === false' ) ; } if ( ( "" >= "x" ) !== false ) { $ERROR ( '#2: ("" >= "x") === false' ) ; } if ( ( "ab" >= "abcd" ) !== false ) { $ERROR ( '#3: ("ab" >= abcd") === false' ) ; } if ( ( "abcd" >= false ) !== true ) { $ERROR ( '#4: ("abcd" >= abc\\u0064") === true' ) ; } if ( ( "x" >= singleExpression & singleExpression & singleExpression [ expressionSequence ] [ singleExpression <= singleExpression ] ) !== false ) { $ERROR ( '#5: ("x" >= "x" + "y") === false' ) ; } var x = "x" ; if ( ( x >= x + numericLiteral ) !== false ) { $ERROR ( '#6: var x = "x"; (x >= x + "y") === false' ) ; }