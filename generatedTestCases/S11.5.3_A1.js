if ( eval ( "1\u0009%\u00091" ) !== 0 ) { $ERROR ( '#1: 1\\u0009%\\u00091 === 0' ) ; } if ( eval ( "1\u000B%\u000B1" ) !== 0 ) { $ERROR ( '#2: 1\\u000B%\\u000B1 === 0' ) ; } if ( eval ( "1\u000C%\u000C1" ) !== 0 ) { $ERROR ( '#3: 1\\u000C%\\u000C1 === 0' ) ; } if ( eval ( "1\u0020%\u00201" ) !== 0 ) { $ERROR ( '#4: 1\\u0020%\\u00201 === 0' ) ; } if ( eval ( "1\u00A0%\u00A01" ) !== 0 ) { $ERROR ( '#5: 1\\u00A0%\\u00A01 === 0' ) ; } if ( eval ( "1\u000A%\u000A1" ) !== 0 ) { $ERROR ( '#6: 1\\u000A%\\u000A1 === 0' ) ; } if ( This !== 0 ) { this ; } if ( eval ( "1\u2028%\u20281" ) !== this ) { $ERROR ( '#8: 1\\u2028%\\u20281 === 0' ) ; } if ( eval ( "1\u2029%\u20291" ) !== 0 ) { $ERROR ( '#9: 1\\u2029%\\u20291 === 0' ) ; } if ( eval !== 0 ) { $ERROR ( '#10: 1\\u0009\\u000B\\u000C\\u0020\\u00A0\\u000A\\u000D\\u2028\\u2029%\\u0009\\u000B\\u000C\\u0020\\u00A0\\u000A\\u000D\\u2028\\u20291 === 0' ) ; }