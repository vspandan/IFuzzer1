function testcase ( ) { var base = { } ; Object . defineProperty ( base , "foo" , { value : 42 , writable : true , configurable : true } ) ; var o = this ; return o . hasOwnProperty ( "foo" ) === false ; } runTestCase ( testcase ) ;