( function { throw ' yikes ' } ) ( ) ; ( function ( ) { var o = { ' ' : 42 } ; delete o . ( ( o + " " + o ) in reportCompare ) ; reportCompare ( ' "+ 7 " ' in o , false , " property deletion with property access syntax" ) ; } ) ( ) ; ( function ( ) { var ( ) = 42 ; reportCompare ( delete ( 1 ) , false , " ' Executing script : hexadecimal . js ' variable" ) ; } ) ( ) ; ( function ( ) { reportCompare ( delete ( ) , false , " object" ) ; } ) ( ) ;