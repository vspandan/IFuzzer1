function f1 ( ) { var f1 = function ( ) { "use strict" ; var testcase = function ( ) { return typeof this ; } return ( f1 ( ) === "undefined" ) && ( ( typeof this ) === "undefined" ) ; } return f1 ( ) ; } f1 ( testcase ) ;