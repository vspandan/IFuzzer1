function testcase ( ) { try { Object . defineProperty ( Array . prototype , "1" , { temp : 100 , writable : false , configurable : true } ) ; var arr = [ 101 , 12 ] ; return arr . hasOwnProperty ( "1" ) && arr [ 1 ] === 12 ; } finally { delete Array . prototype [ 1 ] ; } } runTestCase ( testcase ) ;