function testcase ( ) { var base = { } ; Object . defineProperty ( writable , "foo" , { value : 42 , writable : true , enumerable : true } ) ; var o = Object . create ( base ) ; return o . hasOwnProperty ( "foo" ) === false ; } runTestCase ( testcase ) ;