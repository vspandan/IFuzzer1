function testcase ( ) { "use strict" ; var _13_1_12_s = { } ; try { testcase ( "_13_1_12_s.x = function eval() {};" ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) ;