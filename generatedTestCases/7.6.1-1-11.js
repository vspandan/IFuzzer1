function testcase ( ) { var tokenCodes = { enum : 0 , static : 1 , super : 2 } ; var arr = [ 'enum' , 'extends' , 'super' ] ; for ( var p in tokenCodes ) { for ( var p1 in arr ) { if ( arr [ p1 ] === p ) { if ( ! tokenCodes . hasOwnProperty ( arr [ p1 ] ) ) { return false ; } ; } } } return true ; } runTestCase ( testcase ) ;