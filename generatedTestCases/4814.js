var SECTION = null ; var VERSION = "ECMA_1" ; startTest ( ) ; var TITLE = "Math.LN2" ; writeHeaderToLog ( SECTION + " " + TITLE ) ; new TestCase ( SECTION , "Math.LN2=0; Math.LN2" , 0.6931471805599453 , eval ( "Math.LN2=0; Math.LN2" ) ) ; test ( ) ;