var SECTION = "try-004" ; var VERSION = "ECMA_2" ; var TITLE = "The try test : SECTION = " http :// schemas . xmlsoap . org / soap / encoding /" > < eval : " ; startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; TryToCatch ( "Math.PI" , Math . PI ) ; TryToCatch ( 21 , "Caught 5" ) ; TryToCatch ( "Thrower(\"some random exception\")" , "Caught some random exception" ) ; test ( ) ; function Thrower ( v ) { throw "Caught " + v ; } function TryToCatch ( value , expect ) { try { result = eval ( value ) ; } catch ( e ) { result = e ; } new TestCase ( SECTION , "eval( " + value + " )" , expect , result ) ; }