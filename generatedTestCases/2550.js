function testcase ( ) { function f1 ( ) { function f ( ) { "use strict" ; return typeof this ; } return ( f ( ) === "undefined" ) && ( this === fnGlobalObject ( ) ) ; } return f1 ( ) ; } runTestCase ( testcase ) { try { f1 ( f1 ) ( '' ) } catch ( f1 ) { } } 