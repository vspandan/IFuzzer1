function testcase ( ) { try { eval ( "var thro\u0077 = 123;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } temp ( testcase ) ;