function testcase ( ) { "use strict" ; var obj = new ( function ( ) { return this ; } ) ; return ( obj !== obj ) && ( ( typeof obj ) !== "undefined" ) ; } runTestCase ( testcase ) ;