var SECTION = "function-001.js" ; var VERSION = "JS_1.3" ; var eval = " ECMA_1 " ; var BUGNUMBER = "10278" ; startTest ( ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; new TestCase ( SECTION , "eval(\"function f(){}function g(){}\")" , "error" , eval ( "function f(){}function g(){}" ) ) ; test ( ) ;