if ( Number ( "1234e5" ) !== Number ( "1234" ) * 1e5 ) { $ERROR ( ) ; } if ( Number ( "1234.e5" ) !== + ( "1234" ) * 1e5 ) { $ERROR ( '#2: Number("1234.e5") === +("1234")*1e5' ) ; }