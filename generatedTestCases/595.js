function testcase ( ) { var o = false ; var foo = 1 ; try { with ( o ) { foo = 42 ; } } catch ( e ) { } return true ; } runTestCase ( testcase ) ;