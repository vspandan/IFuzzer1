function testcase ( ) { 'use strict' ; try { eval ( 'function foo() { var eval = 42, a;}' ) ; return false ; } catch ( e ) { return ( e instanceof SyntaxError ) ; } } eval ( testcase ) ;