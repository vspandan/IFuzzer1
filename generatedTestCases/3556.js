var SECTION = "lexical-011" ; var VERSION = "JS1_4" ; var TITLE = "Future Reserved Words" ; startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; print ( "this test requires option javascript.options.strict enabled" ) ; if ( ! options ( ) . match ( /strict/ ) ) { options ( 'strict' ) ; } if ( ! options ( ) . match ( /werror/ ) ) { options ( 'werror' ) ; } var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { eval ( "super = true;" ) ; } catch ( e ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( TITLE , "super = true" + " (threw " + exception + ")" , expect , result ) ; test ( ) ;