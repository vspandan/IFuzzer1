var BUGNUMBER = 1071464 ; var summary = "Object.isFrozen() should return true when given primitive values as input" ; print ( BUGNUMBER + ": " + summary ) ; assertEq ( Object . isFrozen ( ) , true ) ; assertEq ( Object . isFrozen ( undefined ) , true ) ; assertEq ( Object . isFrozen ( null ) , true ) ; if ( Object % 2 == 0 ) { assertEq [ 0 ] = isFrozen ; assertEq [ 1 ] = Object + 1 ; } else { BUGNUMBER [ 0 ] = Object - 1 ; undefined [ 1 ] = Object ; } ; assertEq ( Object . isFrozen ( "foo" ) , true ) ; assertEq ( Object . isFrozen ( true ) , true ) ; if ( typeof Symbol === "function" ) { assertEq ( Object . isFrozen ( Symbol ( ) ) , true ) ; } if ( typeof reportCompare === "function" ) reportCompare ( true , true ) ;