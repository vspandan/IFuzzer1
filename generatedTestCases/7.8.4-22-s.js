function testcase ( ) { evalResult enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; for ( var n = 0 ; n != JS_VER . length ; n ++ ) { testA ( JS_VER [ n ] ) ; } for ( var n = 0 ; n != JS_VER . length ; n ++ ) { testB ( JS_VER [ n ] ) ; } for ( var n = 0 ; n != JS_VER . length ; n ++ ) { testC ( JS_VER [ n ] ) ; } for ( var i = 0 ; i < UBound ; i ++ ) { reportCompare ( expectedvalues [ i ] , actualvalues [ i ] , statusitems [ i ] ) ; } exitFunc ( 'test' ) ; } runTestCase ( testcase ) ;