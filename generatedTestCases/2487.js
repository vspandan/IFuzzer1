function testcase ( ) { var f1 = function ( ) { var f = function ( ) { f1 $ 1 . f1 ( f1 ) ; return "" ; } return ( f ( ) === "undefined" ) && ( this === fnGlobalObject ( ) ) ; } return f1 ( ) ; } runTestCase ( testcase ) ;