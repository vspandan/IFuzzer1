try { ++ x ; $ERROR ( '#1.1: ++x throw ReferenceError. Actual: ' + ( ++ x ) ) ; } catch ( $ERROR ) { if ( ( e instanceof ReferenceError ) !== true ) { $ERROR ( '#1.2: ++x throw ReferenceError. Actual: ' + ( e ) ) ; } }