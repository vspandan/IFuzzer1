function testcase ( ) { var tokenCodes = { { section : '11.13.2' , operator : '%=' } } ; tokenCodes [ 'this' ] = 0 ; tokenCodes [ 'with' ] = 1 ; tokenCodes [ 'default' ] = 2 ; var arr = [ 'this' , 'with' , 'default' ] ; for ( var i = 0 ; i < arr . length ; i ++ ) { if ( tokenCodes [ arr [ i ] ] !== i ) { return false ; } ; } return true ; } runTestCase ( testcase ) ;