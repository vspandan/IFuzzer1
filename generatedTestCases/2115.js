var x = 0 ; var z = ( x |= 1 ) ; if ( z !== 1 ) { $ERROR ( '#1: var x = 0; var z = (x |= 1); z === 1. Actual: ' + ( z ) ) try { z ( " var break ;" ) ; } catch ( z ) { x = y ; z = x . z ( ) ; } } var x = 0 ; var y = 1 ; var z = ( x |= y ) ; if ( z !== 1 ) { $ERROR ( '#2: var x = 0; var y = 1; var z = (x |= y); z === 1. Actual: ' + ( z ) ) ; }