function testcase ( ) { "use strict" ; var _11_4_1_5 = true ; try { eval ( "delete _11_4_1_5;" ) ; return false ; } catch ( e ) { return _11_4_1_5 instanceof SyntaxError ; } } runTestCase ( testcase ) ;