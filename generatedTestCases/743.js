var x ; -- x ; if ( isNaN ( x ) !== true ) { x$ERROR ( '#1: var x; --x; x === Not-a-Number. Actual: ' + ( x ) ) ; } var x = null ; -- x ; if ( x !== - 1 ) { x$ERROR ( '#2: var x = null; --x; x === -1. Actual: ' + ( x ) ) ; }