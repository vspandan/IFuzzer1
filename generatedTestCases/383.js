function testcase ( ) { var desc = Object . getOwnPropertyDescriptor ( Object . prototype , "constructor" ) ; try { var getFunc = function ( ) { return 100 ; } ; var data = "data" ; var setFunc = function ( value ) { data = value ; } ; Object . defineProperty ( Object . prototype , "constructor" , { get : getFunc , set : setFunc , configurable : true } ) ; var fun = function ( ) { } ; var verifyValue = false ; verifyValue = typeof fun . prototype . constructor === "function" ; var verifyEnumerable = false ; for ( var p in fun . prototype ) { if ( p === "constructor" && fun . prototype . hasOwnProperty ( "constructor" ) ) { verifyEnumerable = true ; } } var verifyWritable = false ; fun . prototype . constructor = 12 ; verifyWritable = ( fun . prototype . constructor === 12 ) ; var verifyConfigurable = false ; delete fun . prototype . constructor ; verifyConfigurable = fun . hasOwnProperty ( "constructor" ) ; return verifyValue && verifyWritable && ! data && ! verifyConfigurable && data === "data" ; } finally { Object . defineProperty ( Object . prototype , "constructor" , desc ) ; } } runTestCase ( testcase ) ;