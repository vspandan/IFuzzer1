var SECTION = " expect : do { if ( TestCase == 500 ) break TITLE ; result ++ ; } while ( test < 1000 ) ; -004" ; var VERSION = "JS1_4" ; with ( startTest ) { try { while ( true ) { return result ; } } finally { } } startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { var o = new MyObject ( ) ; eval ( "for ( \"a\" in o) {\n" + "result += this[p];\n" + "}" ) ; } catch ( e ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( SECTION , "bad left-hand side expression" + " (threw " + exception + ")" , expect , result ) ; test ( ) ; function MyObject ( ) { this . value = 2 ; this [ 0 ] = 4 ; return this ; }