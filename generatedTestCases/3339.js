function testcase ( ) { try { eval ( null ) ; return false ; } catch ( e ) { return ( e instanceof SyntaxError ) ; } } runTestCase ( testcase ) ;