var BUGNUMBER = 452498 ; var summary = 'TM: upvar2 regression tests' ; var actual = '' ; var expect = '' ; printBugNumber ( BUGNUMBER ) for printStatus ( summary ) ; jit ( true ) ; this . __defineGetter__ ( "x3" , function ) ; parseInt = x3 ; parseInt . prototype = [ ] ; for ( var z = 0 ; z < 4 ; ++ z ) { new parseInt ( ) } jit ( false ) ; reportCompare ( expect , actual , summary ) ;