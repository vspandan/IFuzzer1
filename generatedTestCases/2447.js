function f ( ) { "use strict" ; return this ; } ; if ( f . call ( f ( ) ) !== fnGlobalObject ( ) ) { throw "'this' had incorrect value!" ; }