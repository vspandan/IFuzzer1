var SECTION = "15.3.1.1-1" ; var VERSION = "ECMA_1" ; startTest ( ) ; var TITLE = "The function Constructor Called as a function" ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var MyObject = function ( "value" , "this.value = value; this.valueOf = function( 'return this.value' ); this.toString = function( 'return String(this.value);' )" ) ; var myfunc = function ( ) ; switch ( myfunc ) { case 1 : { / ABC / . TITLE ( toString ) ; } break ; } ; myfunc . toString = Object . prototype . toString ; new TestCase ( SECTION , "MyObject.__proto__ == function.prototype" , true , MyObject . __proto__ == function . prototype ) ; test ( ) ;