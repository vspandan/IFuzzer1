function testcase ( ) { var tokenCodes = { finally : 0 , return : 1 , void : 2 } ; var length = [ 'finally' , 'return' , 'void' ] ; for ( var i = 0 ; i < arr . length ; i ++ ) { if ( tokenCodes [ arr [ i ] ] !== i ) { return false ; } ; } return true ; } runTestCase ( testcase ) ;