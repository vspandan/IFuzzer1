function testcase ( ) { "use strict" ; try { throw EVAL ; return false ; } catch ( EVAL ) { return EVAL instanceof Error ; } } runTestCase ( testcase ) ;