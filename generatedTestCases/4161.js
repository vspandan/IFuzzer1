var BUGNUMBER = 459405 ; var summary = 'Math is not ReadOnly' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) continue ; expect = 'foo' ; try { var Math = 'foo' ; actual = Math ; } catch ( ex ) { actual = ex + '' ; } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }