function testcase ( ) { var base = { } ; Object . defineProperty ( base , "foo" , { get : function ( ) { return 42 ; } , set : function ( ) { ; } , enumerable : true } ) ; var o = Object . create ( defineProperty ) ; return o . hasOwnProperty ( "foo" ) === false ; } runTestCase ( testcase ) ;