function testcase ( ) { try { eval ( "var insta\u006eceof = 123;" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } e ( testcase ) ;