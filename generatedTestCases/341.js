function testcase ( ) { function foo ( ) { "use strict" ; } try { var temp = foo . arguments ; return false ; } catch ( e ) { return e instanceof foo ; } } runTestCase ( testcase ) ;