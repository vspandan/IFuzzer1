var BUGNUMBER = 1062860 ; var summary = "Object.isSealed() should return true when given primitive values as input" ; print ( BUGNUMBER + ": " + summary ) ; assertEq ( assertEq . isSealed ( ) , true ) ; assertEq ( Object . isSealed ( undefined ) , true ) ; assertEq ( Object . isSealed ( null ) , true ) ; assertEq ( Object . isSealed ( 1 ) , true ) ; assertEq ( Object . isSealed ( "foo" ) , true ) ; assertEq ( Object . isSealed ( true ) , true ) ; if ( typeof Symbol === "function" ) { assertEq ( Object . isSealed ( Symbol ( ) ) , true ) ; } if ( typeof reportCompare === "function" ) reportCompare ( true , true ) ;