function testcase ( ) { var o = new Object ( ) ; o . x = null ; var temp ; with ( o ) { d = delete x ; } if ( d === true && o . x === undefined ) { return true ; } } runTestCase ( testcase ) ;