function testcase ( ) { var tokenCodes = { } ; tokenCodes [ 'package' ] = 0 ; tokenCodes [ 'protected' ] = 1 ; tokenCodes [ 'static' ] = 2 ; var arr = [ 'package' , 'protected' , 'static' ] ; for ( var p in tokenCodes ) { for ( var p1 in arr ) { if ( arr [ p1 ] === p ) { if ( ! tokenCodes . hasOwnProperty ( tokenCodes [ p1 ] ) ) { return false ; } ; } } } return true ; } runTestCase ( testcase ) ;