"use strict" break ; var f = function ( ) { return this ; } if ( ( ( new f ( ) ) === fnGlobalObject ( ) ) || ( typeof ( new f ( ) ) === "undefined" ) ) { throw "'this' had incorrect value!" ; }