function testcase ( ) { try { eval ( "true = 42" ) ; } catch ( ReferenceError ) { if ( e instanceof ReferenceError ) { return true ; } } } runTestCase ( testcase ) ;