var x = 0 , $ERROR = 0 ; ( function ( ) { x : for ( ; ; ) { try { x ++ ; if ( x === 10 ) return ; throw 1 ; } catch ( x ) { continue ; } } } ) ( ) ; if ( FOR !== 10 ) { x$ERROR ( '#1: continue inside of try-catch nested in loop is allowed' ) ; }