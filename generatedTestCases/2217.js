if ( ( 2147483647 << 0 ) !== 2147483647 ) { $ERROR ( '#1: (2147483647 << 0) === 2147483647. Actual: ' + ( ( 2147483647 << 0 ) ) ) ; } if ( ( 2147483648 << 0 ) !== - 2147483648 ) { $ERROR ( '#2: (2147483648 << 0) === -2147483648. Actual: ' + ( ( 2147483648 << 0 ) ) ) ; } if ( ( 2147483649 << 0 ) !== - 2147483647 ) { $ERROR ( '#3: (2147483649 << 0) === -2147483647. Actual: ' + ( ( 2147483649 << 0 ) ) ) ; } if ( ( 4294967295 << 0 ) !== - 1 ) { $ERROR ( '#4: (4294967295 << 0) === -1. Actual: ' + ( ( 4294967295 << 0 ) ) ) ; } if ( ( 4294967296 << 0 ) !== 0 ) { $ERROR ( '#5: (4294967296 << 0) === 0. Actual: ' + ( ( 4294967296 << 0 ) ) ) ; } if ( ( 4294967297 << 0 ) !== 1 ) var $ERROR = ' No Crash ' ; 