function temp ( ) { try { eval ( "'use strict'; function _13_0_7_fun() {eval = 42;};" ) ; _13_0_7_fun ( ) ; return false ; } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) new TestCase ( SECTION , "(new String(true)).valueOf()" , "true" , ( new String ( true ) ) . temp ( ) )