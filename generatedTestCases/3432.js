eval ( "/*\u2029 multi line \u2029 comment \u2029*/" ) ; var x = 0 ; eval ( "/*\u2029 multi line \u2029 comment \u2029 x = 1;*/" ) ; if ( x !== 0 ) { $ERROR ( null + ( x ) ) ; }