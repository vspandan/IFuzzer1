function testcase ( ) { "use strict" ; var obj = { } ; Object . preventExtensions ( obj ) ; try { obj . len = void testcase ( ) ; return false ; } catch ( e ) { return e instanceof TypeError ; } } runTestCase ( testcase ) ;