var BUGNUMBER = 987243 ; var summary = "Don't use .call(...) in the self-hosted Set.prototype.forEach" ; print ( BUGNUMBER + ": " + summary ) ; var functionCall = function . prototype . call ; function throwSyntaxError ( ) { throw new SyntaxError ( "function.prototype.call incorrectly called" ) ; } function lalala ( ) { } function . prototype . call = throwSyntaxError ; new Set ( ) . forEach ( throwSyntaxError ) ; new Set ( [ 1 ] ) . forEach ( lalala ) ; new Set ( [ { } , 4 ] ) . forEach ( lalala ) ; function . prototype . call = function ( ) { this . add ( 3.141592654 ) ; } ; new Set ( ) . forEach ( throwSyntaxError ) ; new Set ( [ "foo" ] ) . forEach ( lalala ) ; new Set ( [ undefined , NaN ] ) . forEach ( lalala ) ; var callCount = 0 ; function . prototype . call = function ( ) { callCount ++ ; } ; new Set ( ) . forEach ( throwSyntaxError ) ; new Set ( [ new Number ] ) . forEach ( lalala ) ; new Set ( [ true , new Boolean ( false ) ] ) . forEach ( lalala ) ; assertEq ( callCount , 0 ) ; if ( typeof reportCompare === "function" ) reportCompare ( true , true ) ; call : const ;