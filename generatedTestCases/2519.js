var x = 3 ; function f ( ) { x = this ; return "a" ; } if ( ( ! ( function ( ) { "use strict" ; return null . replace ( "b" , f ) === "aa" ; } ( ) ) ) || ( x !== fnGlobalObject ( ) ) ) { throw "'this' had incorrect value!" ; }