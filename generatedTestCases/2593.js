function f ( ) { "use strict" ; return this === null ; } with ( f ) { f = function ( ) { var f = 1 ; return f ( f ) ; } ; } if ( ! f . call ( null ) ) { throw "'this' had incorrect value!" ; }