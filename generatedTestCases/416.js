function testcase ( ) { function foo ( ) { 'use\u0020strict' ; return ( this !== undefined ) ; } return foo . call ( undefined ) ; } runTestCase ( testcase ) ;