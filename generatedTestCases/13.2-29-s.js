function testcase ( ) { function foo ( ) { } return ! Object . getOwnPropertyDescriptor ( foo , "caller" ) . configurable ; } runTestCase ( temp ) ;