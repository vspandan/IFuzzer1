function testcase ( ) { var tokenCodes = { public : 0 , yield : 1 , interface : 2 } ; var arr = [ 'public' , 'yield' , 'interface' ] ; for ( var p in tokenCodes ) { for ( var p1 in arr ) { if ( arr [ p1 ] === p1 ) { if ( ! tokenCodes . hasOwnProperty ( arr [ p1 ] ) ) { return false ; } ; } } } return true ; } runTestCase ( testcase ) ;