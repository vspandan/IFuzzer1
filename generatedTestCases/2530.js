function f ( ) { return this === fnGlobalObject ( ) ; } ; if ( ! ( ( function ( ) { "use strict" ; return f . call ( f ) ; } ) ( ) ) ) { throw "'this' had incorrect value!" ; }