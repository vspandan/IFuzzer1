var SECTION = "11.2.2-9-n.js" ; var VERSION = "ECMA_1" ; startTest ( ) ; var TITLE = "The new operator" ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var TITLE ; new TestCase ( SECTION , "var FUNCTION = new function(); f = new FUNCTION(); typeof f" , "object" , eval ( "var FUNCTION = new function(); f = new FUNCTION(); typeof f" ) ) ; new TestCase ( SECTION , "var FUNCTION = new function('return this'); f = new FUNCTION(); typeof f" , "object" , eval ( "var FUNCTION = new function('return this'); f = new FUNCTION(); typeof f" ) ) ; test ( ) ;