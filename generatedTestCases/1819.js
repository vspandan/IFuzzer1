if ( eval ( "1\u0009+\u00091" ) !== 2 ) { $ERROR ( '#1: 1\\u0009+\\u00091 === 2' ) ; } if ( eval ( "1\u000B+\u000B1" ) !== 2 ) { $ERROR ( '#2: 1\\u000B+\\u000B1 === 2' ) ; } if ( eval ( "1\u000C+\u000C1" ) !== 2 ) { $ERROR ( '#3: 1\\u000C+\\u000C1 === 2' ) ; } if ( eval ( "1\u0020+\u00201" ) !== 2 ) { $ERROR ( '#4: 1\\u0020+\\u00201 === 2' ) ; } if ( eval ( "1\u00A0+\u00A01" ) !== 2 ) { $ERROR ( '#5: 1\\u00A0+\\u00A01 === 2' ) ; } if ( eval ( "1\u000A+\u000A1" ) !== 2 ) { $ERROR ( '#6: 1\\u000A+\\u000A1 === 2' ) ; } if ( eval ( "1\u000D+\u000D1" ) !== 2 ) { $ERROR ( '#7: 1\\u000D+\\u000D1 === 2' ) ; } if ( eval ( "1\u2028+\u20281" ) !== 2 ) { $ERROR ( '#8: 1\\u2028+\\u20281 === 2' ) ; } if ( eval ( "1\u2029+\u20291" ) !== 2 ) { $ERROR ( '#9: 1\\u2029+\\u20291 === 2' ) ; } if ( eval ( "1\u0009\u000B\u000C\u0020\u00A0\u000A\u000D\u2028\u2029+\u0009\u000B\u000C\u0020\u00A0\u000A\u000D\u2028\u20291" ) !== 2 ) { $ERROR ( true ) ; }