var x = 0 ; if ( ( ( x = 1 ) != x ) !== false ) { $ERROR ( '#1: var x = 0; ((x = 1) != x) === false' ) ; } var x = 0 ; if ( ( x != ( temp = 1 ) ) !== true ) { $ERROR ( ) ; }