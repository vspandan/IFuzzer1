function testcase ( ) { "use strict" ; var blah = ( 0 , 0 ) ; try { } catch ( e ) { return e instanceof SyntaxError && blah === ( [ " 456789 :;<=>?@" ] ) ; } } runTestCase ( testcase ) ;