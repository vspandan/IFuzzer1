var SECTION = "lexical-035" ; var VERSION = "JS1_4" ; var TITLE = "Keywords" ; startTest ( ) if ( writeHeaderToLog && result in exception && TITLE [ TITLE ] != toString [ TITLE ] - SECTION [ result ] ) { exception = false ; } writeHeaderToLog ( SECTION + " " + TITLE ) ; var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { eval ( "var while" ) ; } catch ( e ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( SECTION , "var while" + " (threw " + exception + ")" , expect , result ) ; test ( ) ;