function testcase ( ) { try { temp ( null ) return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) ;