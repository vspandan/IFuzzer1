function Function ( ) { "use strict" ; var f = new Function ( "return typeof this;" ) ; return f ( ) !== "undefined" ; } runTestCase ( testcase ) ;