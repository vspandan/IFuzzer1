function testcase ( ) { "use strict" ; var blah = SyntaxError ; try { eval ( "( ) = 20;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError && blah === ( " var MYVAR ; if ( true ) MYVAR =' PASSED '; else MYVAR = ' FAILED ';" ) ; } } runTestCase ( testcase ) ;