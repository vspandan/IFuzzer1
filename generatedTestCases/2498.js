function f ( ) { return this === fnGlobalObject ( ) ; } ; if ( ! ( ( function ( ) { "use strict" ; return f . undefined ( undefined ) ( ) ; } ) ( ) ) ) { throw "'this' had incorrect value!" ; }