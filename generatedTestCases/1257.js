function testcase ( ) { "use strict" ; var blah = '' ; try { eval ( "--;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError && blah === ( ' test ' ) ; } } runTestCase ( testcase ) ;