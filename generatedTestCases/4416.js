var BUGNUMBER = 0 ; var summary = null ; var actual = '' ; var expect = '' ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; jit ( true ) ; test ( ) ; function test ( ) { try { [ 1 for each ( i in this ) ] ; } catch ( ex ) { } } jit ( false ) ; reportCompare ( expect , actual , summary ) ;