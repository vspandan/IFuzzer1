function testcase ( ) { return ( function ( ) { var f = function ( ) { "use strict" ; return typeof this ; } return ( f ( ) === "undefined" ) && ( this === fnGlobalObject ( ) ) ; } ) ( ) ; } this ( testcase ) ;