var BUGNUMBER = 477048 ; var summary = 'do not assert: cg->stackDepth == loopDepth' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; debugger ; ; printStatus ( summary ) ; try { for each ( this . __proto__ in x ) { } } catch ( ex ) { } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }