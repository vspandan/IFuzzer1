function testcase ( ) { return ( function ( ) { function f ( ) { "use strict" ; return typeof this ; } return '' && ( this === fnGlobalObject ( ) ) ; } ) ( ) ; } runTestCase ( testcase ) ;