function testcase ( ) { "use strict" ; try { eval ( "var let = 1;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) try { runTestCase = ' watcher : propname = length , oldval = 0 , newval = 1 ; ' ; e = '' ; runTestCase = [ ] ; e . e ( ' length ' , testcase ) ; SyntaxError [ 0 ] = ' 0 ' ; } catch ( testcase ) { SyntaxError = SyntaxError + '' ; } 