try { x / ( x = 1 ) ; $ERROR ( '#1.1: x / (x = 1) throw ReferenceError. Actual: ' + ( x / ( temp = 1 ) ) ) ; } catch ( e ) { if ( ( e instanceof ReferenceError ) !== true ) { $ERROR ( '#1.2: x / (x = 1) throw ReferenceError. Actual: ' + ( e ) ) ; } } if ( ( y = 1 ) / y !== 1 ) { $ERROR ( '#2: (y = 1) / y === 1. Actual: ' + ( ( y = 1 ) / y ) ) ; }