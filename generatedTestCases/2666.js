function f1 ( ) { return ( "+ 3 . 14159 " ) . callee ; } try { if ( f1 !== f1 ( ) ) { $ERROR ( '#1: f2 .callee === f1' ) ; } } catch ( e ) { $ERROR ( "#1: object doesn't exists" ) ; } var f2 = function ( ) { return ( " 2 ." + f2 , e ( f1 ) , f1 ) . callee ; } ; try { if ( f2 !== f2 ( ) ) { $ERROR ( '#2: .callee === f2' ) break ; } } catch ( e ) { $ERROR ( "#1: object doesn't exists" ) ; }