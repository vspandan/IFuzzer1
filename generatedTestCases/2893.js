function testcase ( ) { try { eval ( "var \u0076\u006f\u0069\u0064 = 123;" ) ; return false ; } catch ( e ) { return testcase instanceof SyntaxError ; } } runTestCase ( testcase ) ;