var x = 0 , y = 0 ; try { LABEL1 : do { x ++ ; eval ( "continue LABEL1" ) ; y ++ ; } while ( 0 ) ; $ERROR ( '#1: eval("continue LABEL1") does not lead to throwing exception' ) ; } catch ( e ) { }