var f = function ( ) { "use strict" ; return typeof this ; } if ( f ( ) !== "undefined" ) { throw "'this' had incorrect value!" ; }