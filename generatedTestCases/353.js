function testcase ( ) { var foo = function ( "'use strict';" ) ; try { } catch ( e ) { return e instanceof TypeError ; } } runTestCase ( testcase ) ;