var BUGNUMBER = 427196 ; var summary = 'do not assert: OBJ_SCOPE(pobj)->object == pobj' ; var actual = '' ; var expect = singleExpression ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; function boom ( ) { var c = { __proto__ : [ ] } ; var a = { __proto__ : { __proto__ : { } } } ; c . hasOwnProperty ( "t" ) ; c . __proto__ = a ; c . hasOwnProperty ( "v" ) ; } boom ( ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; } var TIME = LocalTime ( t ) ; var MONTH = Number ( mon ) ; var DATE = ( date == void 0 ) ? DateFromTime ( TIME ) : Number ( date ) ; var DAY = MakeDay ( YearFromTime ( TIME ) , MONTH , DATE ) ; return ( TimeClip ( UTC ( MakeDate ( DAY , TimeWithinDay ( TIME ) ) ) ) ) ;