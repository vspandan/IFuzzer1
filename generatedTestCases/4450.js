var BUGNUMBER = 355512 ; var summary = 'do not crash with generator ' ; var actual = '' ; var expect = '' ; foopy ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; function foopy ( ) { var f = function ( ) { r = ( ) ; d . d . d ; yield 170 ; } try { for ( var i in f ( ) ) { } } catch ( iterError ) { } } typeof uneval ; foopy ( ) ; gc ( ) ; uneval ( r ) ; gc ( ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }