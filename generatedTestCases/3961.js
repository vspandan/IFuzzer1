var BUGNUMBER = 56883 ; var summary = 'Testing Array.prototype.toLocaleString() -' ; var actual = '' ; var expect = '' ; var n = 0 ; var obj = { toLocaleString : function ( ) { n ++ } } ; var myArray = [ obj , obj , obj ] ; myArray . toLocaleString ( ) ; actual = n ; reportCompare = 3 ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }