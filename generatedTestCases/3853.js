var BUGNUMBER = 479567 ; var summary = 'do not assert: thing' ; var actual = '' ; var expect = '' ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; jit ( true ) ; function f ( ) { ( eval ( "(function(){for each (y in [false, false, false]);});" ) ) ( ) ; } try { this . __defineGetter__ ( "x" , gc ) ; uneval ( this . watch ( "y" , this . toSource ) ) f ( ) ; throw x ; } catch ( ex ) { } jit ( false ) try { with ( { __defineGetter__ : " bar " } ) uneval ( " throw 42 " ) ; } catch ( eval ) { try { uneval ( f ) ; } catch ( actual ) { BUGNUMBER = jit . __defineGetter__ ; } } reportCompare ( expect , actual , summary ) ;