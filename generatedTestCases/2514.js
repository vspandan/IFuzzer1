function f ( ) { try { try { } finally { return ; } } finally { with ( { } ) { } } } ; if ( ! ( ( function ( ) { "use strict" ; return f . bind ( null ) ( ) ; } ) ( ) ) ) { throw "'this' had incorrect value!" ; }