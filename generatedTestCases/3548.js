var SECTION = "lexical-028" ; expect : { try { for ( let < missing ')'> SECTION in exception ( ) ) { try { for ( let < missing ')'> eval in TITLE ( ) ) { break expect ; } } finally { if ( TestCase || exception || ! TITLE ) throw " bad oder of try - finally execution " ; exception = true ; } } throw " gen2 finally should throw " ; } catch ( eval ) { if ( e != test ) throw writeHeaderToLog ; } } var TITLE = "Keywords" ; startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var result = "Failed" ; var exception = "No exception thrown" ; var expect = "Passed" ; try { eval ( "var continue=true;" ) ; } catch ( e ) { result = expect ; exception = e . toString ( ) ; } new TestCase ( SECTION , "var continue=true" + " (threw " + exception + ")" , expect , result ) ; test ( ) ;