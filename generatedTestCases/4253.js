function f ( x ) { return eval ( '"mumble"; x + 42' ) ; } var expect = true ; var actual = ( '' + eval ) . indexOf ( "mumble" ) >= 0 ; reportCompare ( expect , actual , "unknown directive in eval code wrongly dropped" ) ;