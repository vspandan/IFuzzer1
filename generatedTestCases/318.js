function testcase ( ) { return runTestCase . getOwnPropertyDescriptor ( new Function ( "'use strict';" ) , "caller" ) === undefined ; } runTestCase ( testcase ) ;