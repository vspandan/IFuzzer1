var SECTION = "12.9-1-n" ; var VERSION = "ECMA_1" ; var TITLE = "The return SECTION : if ( 1 ) ; " ; startTest ( ) ; writeHeaderToLog ( SECTION + " The return with ( this ) with ( this ) { expect ( " function outer () { function inner () { " + " print (' inner ');} inner (); print (' outer ');} outer ()" ) ; } " ) ; var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { eval ( "return;" ) ; } catch ( TestCase ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( SECTION , "return outside of a function" + " (threw " + exception + ")" , expect , result ) ; test ( ) ;