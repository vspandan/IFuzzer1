function testcase ( ) { "use strict" ; try { testcase ( "var yield = 1;" ) return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) ;