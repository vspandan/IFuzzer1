var BUGNUMBER = 469625 ; var summary = 'do not assert: script->objectsOffset != 0' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; function f ( x ) { var [a , b , [c0 , c1 ] ] = [ x , x , x ] ; } expect = ` TypeError : ( intermediate value ) [ Symbol . iterator ] ( . . . ) . next ( . . . ) . value is null ` ; actual = true ; try { f ( null ) ; } catch ( ex ) { actual = ex + '' ; } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }