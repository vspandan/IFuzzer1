function testcase ( ) { var bIsFooCalled = false ; var foo = function ( ) { bIsFooCalled = true function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; singleExpression arguments argumentList block var doc ; if ( typeof document == 'undefined' ) { doc = { } ; } else { doc = document ; } if ( typeof alert == 'undefined' ) { alert = print ; } doc . watch ( "title" , function ( a , b , c , d ) { return { toString : function ( ) { alert ( 1 ) ; } } ; } ) ; doc . title = "xxx" ; doc . watch ( "title" , function ( ) { return { toString : function ( ) { alert ( 1 ) ; } } ; } ) ; doc . title = "xxx" ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; } } ; var d = delete foo ( ) ; if ( d === true && bIsFooCalled === true ) return true ; } runTestCase ( testcase ) ;