var SECTION = "lexical-054" ; var VERSION = "JS1_4" ; var result = 418730 ; startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { a = 0 ; b = 1 ; c = 2 ; d = 3 ; eval ( "if (a > b)\nelse c = d" ) ; } catch ( e ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( SECTION , "if (a > b)\nelse c = d" + " (threw " + exception + ")" , expect , result ) ; test ( ) ;