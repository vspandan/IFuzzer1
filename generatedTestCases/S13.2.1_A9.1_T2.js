var x ; var __func = function ( ) { x = true ; } if ( __func ( ) !== undefined ) { $ERROR ( '#1: __func() === undefined. Actual: __func() ===' + this ( ) ) ; } ; if ( ! x ) { $ERROR ( '#2: x === true. Actual: x === ' + x ) ; }