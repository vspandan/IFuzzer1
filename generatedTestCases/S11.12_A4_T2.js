if ( ( 1 ? 0 : 1 ) !== 0 ) { temp ( '#1: (1 ? 0 : 1) === 0' ) ; } var y = new Number ( 1 ) ; if ( ( 1 ? y : 0 ) !== y ) { $ERROR ( ) ; } var y = new Number ( NaN ) ; if ( ( y ? y : 1 ) !== y ) { $ERROR ( '#3: (var y = new Number(NaN); (y ? y : 1) === y' ) ; }