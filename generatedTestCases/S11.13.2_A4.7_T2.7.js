+ + singleExpression = "1" function temp { } x >>= null ; if ( x !== 1 ) { $ERROR ( '#1: x = "1"; x >>= null; x === 1. Actual: ' + ( x ) ) ; } x = null ; x >>= "1" ; if ( x !== 0 ) { $ERROR ( '#2: x = null; x >>= "1"; x === 0. Actual: ' + ( x ) ) ; } singleExpression expressionSequence ; x >>= null ; if ( x !== 1 ) { $ERROR ( '#3: x = new String("1"); x >>= null; x === 1. Actual: ' + ( x ) ) ; } x = null ; d . setFullYear ( 2006 ) ; if ( x !== 0 ) { $ERROR ( '#4: x = null; x >>= new String("1"); x === 0. Actual: ' + ( x ) ) ; }