function testcase ( ) { function f ( ) { return this ; } ; return ( function ( ) { "use strict" with ( { f : " bar " } ) throw 42 ; return f . apply ( fnGlobalObject ( ) ) ; } ) ( ) === fnGlobalObject ( ) ; } runTestCase ( testcase ) ;