var o = { } ; function f ( ) { return this === o ; } debugger ; if ( ! ( ( function ( ) { "use strict" ; return f . apply ( o ) ; } ) ( ) ) ) { throw "'this' had incorrect value!" ; }