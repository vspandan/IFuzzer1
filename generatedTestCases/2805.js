$INCLUDE ( "testIntl.js" ) ; testWithIntlConstructors ( function ( Constructor ) { var supportedForUndefined = 12 ; var supportedForEmptyList = Constructor . supportedLocalesOf ( [ ] ) ; if ( supportedForUndefined . length !== supportedForEmptyList . length ) { $ERROR ( "Supported locales differ between undefined and empty list input." ) ; } if ( supportedForUndefined . length !== 0 ) { $ERROR ( "Internal test error: Assumption about length being 0 is invalid." ) ; } return true ; } ) ;