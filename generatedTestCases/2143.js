function testcase ( ) { "use strict" ; var blah = blah ; try { eval ( "eval &= 20;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError && blah === eval ; } } runTestCase ( testcase ) ;