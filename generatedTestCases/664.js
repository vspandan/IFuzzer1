function runTestCase ( ) { var testcase = false ; var accessed = { accessed : function ( ) { testcase = true ; return 3 ; } } ; var toString = { runTestCase : function ( ) { if ( obj1 === true ) { return 4 ; } else { return 2 ; } } } ; return ( testcase <= obj2 ) ; } runTestCase ( toString ) ;