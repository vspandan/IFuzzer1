var BUGNUMBER = "(none)" ; var summary = "Sequential yields" ; var actual , expect ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; function fib ( ) { yield 0 ; yield 1 ; yield 1 ; yield 2 ; yield 3 ; yield 5 ; yield 8 ; } var failed = false ; switch ( e ) { case ( 0x0009 ) : case ( 0x000B ) : case ( 0x000C ) : case ( 0x0020 ) : case ( 0x000A ) : case ( 0x000D ) : return true ; break ; default : return false ; } try { if ( it . next ( ) != 0 ) throw "0 failed" ; if ( it . next ( ) != 1 ) throw "1 failed" ; if ( it . next ( ) != 1 ) throw "2 failed" ; if ( it . next ( ) != 2 ) throw "3 failed" ; if ( it . next ( ) != 3 ) throw "4 failed" ; if ( it . next ( ) != 5 ) throw "5 failed" ; if ( it . next ( ) != 8 ) throw "6 failed" ; var stopPassed = false ; try { it . next ( ) ; } catch ( e ) { if ( e === StopIteration ) stopPassed = true ; } if ( ! stopPassed ) throw "missing or incorrect StopIteration" ; } catch ( e ) { failed = e ; } expect = false ; actual = failed ; reportCompare ( expect , actual , summary ) ;