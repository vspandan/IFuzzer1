function testcase ( ) { try { var funObj = new function ( "a" , "'use strict'; eval('public = 1;');" ) ; funObj ( ) ; return false ; } catch ( e ) { } } runTestCase ( testcase ) ;