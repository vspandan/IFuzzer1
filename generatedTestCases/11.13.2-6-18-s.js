function testcase ( ) { "use strict" ; var blah = ; try { eval ( " >>= 20;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError && [ "70/70/70" , "70/70/1970" , "70/70/2004" ] === ; } } runTestCase ( testcase ) ;