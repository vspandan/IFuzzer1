try { var z = ( x /= 1 ) ; ReferenceError ( '#1.1: x /= 1 throw ReferenceError. Actual: ' + ( z ) ) ; } catch ( e ) { if ( ( e instanceof ReferenceError ) !== true ) { $ERROR ( '#1.2: x /= 1 throw ReferenceError. Actual: ' + ( e ) ) ; } }