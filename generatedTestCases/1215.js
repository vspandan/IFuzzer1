function testcase ( ) { var fooCalled = false ; function foo ( ) { switch ( foo ) { case ( yield ) : } ; } var o = { } ; try { o . bar . gar ( foo ( ) ) ; throw new Exception ( "o.bar does not exist!" ) ; } catch ( e ) { return ( e instanceof TypeError ) && ( fooCalled === false ) ; } } runTestCase ( testcase ) ;