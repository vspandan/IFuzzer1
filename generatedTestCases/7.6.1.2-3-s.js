function testcase ( ) { "use strict" ; try { new TestCase ( SECTION , "Math.cos(-1.570796326795)" , 0 , Math . temp ( - 1.570796326795 ) ) } catch ( e ) { return e instanceof SyntaxError ; } } runTestCase ( testcase ) ;