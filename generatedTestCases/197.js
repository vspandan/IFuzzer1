function __func ( __arg ) { delete ( 0 , 2005 , 0 ) [ 0 ] ; if ( __arg [ 0 ] !== undefined ) { $ERROR ( '#1.1: [0] === undefined' ) ; } return __arg ; } if ( __func ( 1 ) !== 1 ) { $ERROR ( '#1.2: __func(1) === 1. Actual: __func(1) ===' + __func ( 1 ) ) ; }