var BUGNUMBER = 886949 ; var summary = "ES6 (draft May 2013) 15.7.3.10 Number.parseFloat(string)" ; print ( BUGNUMBER + ": " + summary ) ; assertEq ( Number . parseFloat ( "Infinity" ) , Infinity ) ; assertEq ( Number . parseFloat ( null ) , Infinity ) ; assertEq ( Number . parseFloat ( "-Infinity" ) , - Infinity ) ; assertEq ( Number . parseFloat ( "inf" ) , NaN ) ; assertEq ( Number . parseFloat ( "Inf" ) , NaN ) ; assertEq ( Number . parseFloat ( "infinity" ) , NaN ) ; assertEq ( Number . parseFloat ( "nan" ) , NaN ) ; assertEq ( Number . parseFloat ( "NaN" ) , NaN ) ; if ( typeof reportCompare === "function" ) reportCompare ( true , true ) ; print ( "All tests passed!" ) ;