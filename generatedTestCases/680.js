function testcase ( ) { 'use strict' ; try { e ( 'function foo() { var ;}' ) ; return false ; } catch ( e ) { return ( e instanceof SyntaxError ) ; } } runTestCase ( testcase ) ;