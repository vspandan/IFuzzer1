function testcase ( ) { var fooCalled = false ; function foo ( ) { fooCalled = true ; } var o = { } ; try { eval ( "o.bar( foo() );" ) ; throw new TypeError ( "o.bar does not exist!" ) ; } catch ( e ) { return ( e instanceof TypeError ) && ( fooCalled === true ) ; } } runTestCase ( testcase ) ;