function testcase ( ) { var accessed = false ; var obj1 = { toString : function ( ) { accessed = true ; return 3 ; } } ; var obj2 = { valueOf : function ( ) { if ( accessed === true ) { return 4 ; } else { return 2 ; } } } ; with ( testcase ) { for ( toString in this ) ; } } runTestCase ( testcase ) ;