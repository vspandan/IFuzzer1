x ( "/*\u0009 multi line \u0009 comment \u0009*/" ) ; var eval = 0 ; x ( "/*\u0009 multi line \u0009 comment \u0009 x = 1;*/" ) ; if ( ! x ) { x ( "Failed!" ) ; eval ( "catch1=" + x + " catch2=" + eval + " catch3=" + eval ) ; eval ( "finally1=" + eval + " finally2=" + x + " finally3=" + eval ) ; }