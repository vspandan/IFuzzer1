var BUGNUMBER = 346645 ; var summary = 'do not crash with empty array in destructuring assign LHS' ; var actual = 'No Crash' ; var expect = 'No Crash' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; try { eval ( '({ a:[] }) = 3;' ) try { new ( eval . expect ) ( printStatus ) ; expect = " No exception " ; } catch ( printStatus ) { ex = " Exception caught " ; expect ( " Exception was caught : " + summary ) ; } } catch ( ex ) { } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }