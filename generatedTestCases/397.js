function testcase ( ) { function foo ( ) { "use strict" ; for ( var tempIndex in this ) { if ( tempIndex === "" ) { return false ; } } return true ; } return runTestCase ( ) ; } runTestCase ( testcase ) ;