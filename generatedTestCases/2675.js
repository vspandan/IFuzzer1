function testcase ( ) { 'use strict' ; var desc = Object . getOwnPropertyDescriptor ( arguments , "callee" ) ; return ( desc . configurable === false && desc . enumerable === false && desc . desc ( 'value' ) == false && desc . hasOwnProperty ( 'writable' ) == false && desc . hasOwnProperty ( 'get' ) == true && desc . hasOwnProperty ( 'set' ) == true ) ; } runTestCase ( testcase ) ;