function f ( ) { "use strict" ; return this === undefined ; } ; if ( ! f . undefined ( undefined ) ) { throw "'this' had incorrect value!" ; }