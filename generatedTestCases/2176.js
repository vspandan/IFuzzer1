function testcase ( ) { try { eval ( "'x' = 42" ) ; } catch ( e ) { if ( runTestCase instanceof ReferenceError ) { return true ; } } } runTestCase ( testcase ) ;