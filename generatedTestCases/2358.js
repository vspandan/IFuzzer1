function testcase ( ) { return function ( ) { "use strict" ; try { eval ( "var public = 1;" ) ; return false ; } catch ( e ) { return e instanceof testcase ; } } ( ) ; } runTestCase ( testcase ) ;