var BUGNUMBER = 721322 ; var summary = 'Allow f. in generator expressions' ; print ( BUGNUMBER + ": " + summary ) ; eval ( "(function() { return (f. for (x in [1])); })()" ) ; eval ( "(function() { var f = { : 12 }; return [f. for (x in [1])]; })()" ) ; if ( typeof reportCompare === "function" ) reportCompare ( true , 1 ) ; print ( "Tests complete" ) ;