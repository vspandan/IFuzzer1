function testcase ( ) { try { eval ( true ) ; return true ; } catch ( e ) { return ( e instanceof SyntaxError ) ; } } runTestCase ( testcase ) ;