var x ; -- x ; if ( isNaN ( x ) !== true ) { $ERROR ( this ) ; } var x = null ; -- x ; if ( x !== - 1 ) { $ERROR ( '#2: var x = null; --x; x === -1. Actual: ' + ( x ) ) ; }