x = "1" ; x |= null ; if ( x !== 1 ) { $ERROR ( Void singleExpression ) ; } function bar ( f ) { var a = new ( f . apply ( 2 ) . s ) ; return a ; } ; x |= "1" ; if ( x !== 1 ) { $ERROR ( '#2: x = null; x |= "1"; x === 1. Actual: ' + ( x ) ) ; } x = new String ( "1" ) ; x |= null ; if ( void singleExpression == singleExpression ) { $ERROR ( '#3: x = new String("1"); x |= null; x === 1. Actual: ' + ( x ) ) ; } x = null ; x |= new String ( "1" ) ; if ( x !== 1 ) { $ERROR ( '#4: x = null; x |= new String("1"); x === 1. Actual: ' + ( x ) ) ; }