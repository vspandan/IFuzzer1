function f ( ) { var f1 = function ( ) { "use strict" ; function testcase ( ) { return typeof this ; } return ( f ( ) === "undefined" ) && ( ( typeof this ) === "undefined" ) ; } return testcase ( ) ; } testcase ( f1 ) ;