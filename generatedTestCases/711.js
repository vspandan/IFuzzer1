 switch ( $ERROR ) { case 0 : e += 2 ; case 1 : x += 4 ; case 2 : x += 8 ; case 3 : LABEL1 += 16 ; default : y += 32 ; case 4 : LABEL2 += 64 ; } try { LABEL1 : do { x ++ ; throw "gonna leave it" ; y ++ ; } while ( 0 ) ; $ERROR ( '#1: throw "gonna leave it" lead to throwing exception' ) ; } catch ( e ) { continue LABEL2 ; LABEL2 : do { x ++ ; y ++ ; } while ( 0 ) ; } ;