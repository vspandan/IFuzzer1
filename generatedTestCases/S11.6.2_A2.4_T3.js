try { x - ( x = 1 ) ; $ERROR ( '#1.1: x - (x = 1) throw ReferenceError. Actual: ' + ( x - ( x = 1 ) ) ) ; } catch ( e ) { if ( ( e instanceof ReferenceError ) !== true ) { } } if ( ( y = 1 ) - y !== 0 ) { $ERROR ( '#2: (y = 1) - y === 0. Actual: ' + ( ( y = 1 ) - y ) ) ; }