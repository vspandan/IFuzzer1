function f1 ( ) { "use strict" ; return ( ( function ( ) { return typeof this ; } ) ( ) === "undefined" ) && ( f1 === "undefined" ) ; } if ( ! f1 ( ) ) { throw "'this' had incorrect value!" ; }