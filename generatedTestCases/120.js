function testcase ( ) { var base = { } ; Object . defineProperty ( base , "foo" , { value : 42 , writable : true } ) ; var o = Object . create ( base ) ; return o . hasOwnProperty ( "foo" ) === false ; } testcase ( testcase ) ;