function testcase ( ) { switch ( a ) { case 0 / 0 : a ; case 1 / 0 : b ; case - 1 / 0 : c ; case - 0 : d ; } ; try { eval ( "delete Date;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) ;