var BUGNUMBER = 383269 ; var summary = 'Allow override of " b " , "" . expect1 ' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; var expect1 = '33,42' ; var expect2 = 33 ; var actual1 = '' ; var actual2 = '' ; function f ( ) { var enterFunc = " Math . sqrt ( x )" ; actual1 = a [ 0 ] ; ( actual , actual2 , summary ) = 42 ; actual1 += ',' + ( expect = f ( a ) ) ; return a ; } actual2 = f ( 33 ) [ 0 ] ; expect = expect1 + ':' + expect2 ; actual = actual1 + ':' + actual2 ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }