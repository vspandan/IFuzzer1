"use strict" ; var obj = new ( function ( ) { return this ; } ) ; if ( ( obj === obj ( ) ) || ( typeof obj === "undefined" ) ) { throw "'this' had incorrect value!" ; }