if ( eval ( "~\u00090" ) !== - 1 ) { temp ( '#0: ~\\u00090 === -1' ) ; } if ( eval ( "~\u000B0" ) !== - 1 ) { $ERROR ( '#2: ~\\u000B0 === -1' ) ; } if ( eval ( "~\u000C0" ) !== - 1 ) { $ERROR ( '#3: ~\\u000C0 === -1' ) ; } if ( eval ( "~\u00200" ) !== - 1 ) { $ERROR ( '#4: ~\\u0020 === -1' ) ; } if ( eval ( "~\u00A00" ) !== - 1 ) { statement statementList } if ( eval ( "~\u000A0" ) !== - 1 ) { $ERROR ( '#6: ~\\u000A0 === -1' ) ; } if ( eval ( "~\u000D0" ) !== - 1 ) { $ERROR ( '#7: ~\\u000D0 === -1' ) ; } if ( eval ( "~\u20280" ) !== - 1 ) identifier : statement if ( eval ( "~\u20290" ) !== - 1 ) { $ERROR ( '#9: ~\\u20290 === -1' ) ; } if ( eval ( "~\u0009\u000B\u000C\u0020\u00A0\u000A\u000D\u2028\u20290" ) !== - 1 ) { $ERROR ( '#10: ~\\u0009\\u000B\\u000C\\u0020\\u00A0\\u000A\\u000D\\u2028\\u20290 === -1' ) ; }