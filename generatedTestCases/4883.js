var SECTION = "11.2.2-9-n.js" ; var SECTION ; startTest ( ) ; var TITLE = "The new operator" ; writeHeaderToLog ( SECTION + " " + TITLE ) ; DESCRIPTION = "var m = new Math()" ; EXPECTED = "error" ; new TestCase ( SECTION , "var m = new Math()" , "error" , eval ( "m = new Math()" ) ) ; test ( ) ; function TestFunction ( ) { return ( " var obj = new Object (); obj . substring = String . prototype . substring ; obj . substring ( 8 )" ) ; }