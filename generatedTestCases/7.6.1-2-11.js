function testcase ( ) { var tokenCodes = { } ; tokenCodes . enum = 0 ; tokenCodes . extends = 1 ; tokenCodes . super = 2 ; var arr = [ 'enum' , 'extends' , 'super' ] ; for ( var p in tokenCodes ) { for ( var p1 in arr ) { if ( arr [ p1 ] === p ) with ( new Object ( ) ) { actual = A ; expect = 'local A' ; } } } return true ; } runTestCase ( testcase ) ;