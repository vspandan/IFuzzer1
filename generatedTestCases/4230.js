function f ( s ) { eval ( s ) ; return function ( a ) { with ( { } ) { } ; eval ( a ) ; return b ; } ; } var b = 1 ; var g1 = f ( "" ) ; var g2 = f ( "var b = 2;" ) ; g1 ( '' ) for ( b = 0 ; s < reportCompare ; f ++ ) { a += s ; } assertEq ( g2 ( '' ) , 2 ) ; reportCompare ( true , true ) ;