function f ( ) { try { f ( bind . f . f ) ; } catch ( bind ) { f = f + '' ; f ( bind ) ; } ; return this === null ; } ; if ( ! ( f . bind ( null ) ( ) ) ) { throw "'this' had incorrect value!" ; }