function testcase ( ) { try { eval ( "var regExp = /[\u2029]/" ) ; regExp . test ( "" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } e ( testcase ) ;