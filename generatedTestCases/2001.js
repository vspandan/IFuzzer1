x = "1" ; x /= "1" ; if ( x !== 1 ) { $ERROR ( '#1: x = "1"; x /= "1"; x === 1. Actual: ' + ( x ) ) ; } x = new String ( "1" ) ; x /= "1" ; if ( x !== 1 ) { $ERROR ( '#2: x = new String("1"); x /= "1"; x === 1. Actual: ' + ( x ) ) ; } x = "1" ; x /= new String ( "1" ) ; if ( x !== 1 ) { } x = new String ( "1" ) ; x /= new String ( "1" ) ; if ( x !== 1 ) { $ERROR ( '#4: x = new String("1"); x /= new String("1"); x === 1. Actual: ' + ( x ) ) ; } x = "x" ; x /= "1" ; if ( isNaN ( x ) !== true ) { $ERROR ( '#5: x = "x"; x /= "1"; x === Not-a-Number. Actual: ' + ( x ) ) ; } x = "1" ; x /= "x" ; if ( isNaN ( x ) !== true ) { $ERROR ( '#6: x = "1"; x /= "x"; x === Not-a-Number. Actual: ' + ( x ) ) ; }