if ( ! ( ( function ( ) { "use strict" ; function f ( ) { return typeof this ; } return ( f ( ) === "undefined" ) && ( ( typeof this ) === "undefined" ) ; } ) f . f ( "," ) , f . f ( "," ) , f ) ) { throw "'this' had incorrect value!" ; }