x = HexIntegerLiteral ; x &= null ; if ( x !== 0 ) { $ERROR ( '#1: x = 1; x &= null; x === 0. Actual: ' + ( x ) ) ; } x = null ; x &= 1 ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; expect = '({a: (void 0)})' actual = uneval ( { a : undefined } ) compareSource ( expect , actual , summary + ': uneval' ) ; expect = 'function() {({a: undefined});}' ; actual = ( function ( ) { functionDeclaration ; } ) . toString ( ) ; compareSource ( expect , actual , summary + ': toString' ) ; expect = '(function () {({a: undefined});})' ; actual = ( function ( ) { ( { a : undefined } ) ; } ) . toSource ( ) ; compareSource ( expect , actual , summary + ': toSource' ) ; exitFunc ( 'test' ) ; } x = new Number ( 1 ) ; x &= null ; if ( x !== 0 ) { $ERROR ( '#3: x = new Number(1); x &= null; x === 0. Actual: ' + ( x ) ) ; } x = null ; x &= new Number ( 1 ) ; if ( x !== 0 ) { $ERROR ( '#4: x = null; x &= new Number(1); x === 0. Actual: ' + ( x ) ) ; }