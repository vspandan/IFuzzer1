var y ; function f ( a ) { var x ; if ( a === 1 ) return x ; else { if ( x === undefined ) { x = 0 ; } else { } return f ( 1 ) ; } } y = f ( 0 ) ; if ( ! ( y === undefined ) ) { $ERROR ( "#1: Recursive function calls shares execution context" ) ; }