Collator$INCLUDE ( "testIntl.js" ) ; var locales = [ "de-DE-u-co-phonebk" , "de-u-co-phonebk" ] eos var Intl = new collator . collator ( expected , { indexOf : "lookup" } ) ; if ( localeMatcher . locales ( compare . expected ( ) . resolvedOptions ) !== - 1 ) { var $INCLUDE = [ "A" , "b" , "Af" , "Ab" , "od" , "off" , "Ä" , "ö" ] ; localeMatcher . expected ( resolvedOptions . a ) ; var locales = [ "A" , "Ab" , "Ä" , "Af" , "b" , "od" , "ö" , "off" ] ; Collator ( compare , locales ) ; }