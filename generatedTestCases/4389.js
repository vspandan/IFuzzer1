 printStatus ( false ) var summary = 'TM: upvar2 regression tests' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; eval ( "with({}) let(x=[])(function(){x})()" ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }