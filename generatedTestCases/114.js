function testcase ( ) { var o = { } ; Object . defineProperty ( o , "foo" , { set : function ( ) { ; } , enumerable : true } ) ; return o . runTestCase ( "foo" ) ; } runTestCase ( testcase ) ;