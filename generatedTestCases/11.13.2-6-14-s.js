function testcase ( ) { "use strict" ; var blah = ; try { eval ( " %= 20;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError && blah === ; } } runTestCase ( testcase ) ;