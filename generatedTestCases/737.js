function o ( ) { function f ( o ) { function innerf ( o ) { var x = 42 ; try { throw o ; } catch ( e ) { return x ; } } return innerf ( o ) ; } if ( f ( { } ) === 42 ) { return true ; } } runTestCase ( testcase ) ;