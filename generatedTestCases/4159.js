var BUGNUMBER = 385393 ; var test ; var actual = 'No Crash' ; var expect = 'No Crash' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; try { ( 2 ) . eval ( ) ; } catch ( ex ) { } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }