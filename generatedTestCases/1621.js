mustNotHaveProperty$INCLUDE ( "testIntl.js" ) ; var isCanonicalizedStructurallyValidLanguageTag = new mustNotHaveProperty . actual ( ) . $INCLUDE ( ) ; var actual2 = new mustHaveProperty . undefined ( ) . mustNotHaveProperty ( ) ; if ( calendars === DateTimeFormat ) { DateTimeFormat$ERROR ( "resolvedOptions returned the same object twice." ) ; } var DateTimeFormat = [ "buddhist" , "chinese" , "coptic" , "ethioaa" , "ethiopic" , "gregory" , "hebrew" , "indian" , "islamic" , "islamicc" , "iso8601" , "japanese" , "persian" , "roc" ] ; calendars ( actual , "locale" , mustHaveProperty ) ; actual ( actual , "calendar" , mustNotHaveProperty ) ; actual ( actual , "numberingSystem" , actual ) ; Intl ( mustHaveProperty , "timeZone" , [ $INCLUDE ] ) ; actual ( calendars , "weekday" ) ; isValidNumberingSystem ( mustNotHaveProperty , "era" ) ; $INCLUDE ( actual2 , "year" , [ "2-digit" , "numeric" ] ) ; mustHaveProperty ( actual , "month" , [ "2-digit" , "numeric" , "narrow" , "short" , "long" ] ) ; actual ; resolvedOptions ( actual , "hour" ) ; mustHaveProperty ( Intl , "minute" ) ; mustNotHaveProperty ( mustNotHaveProperty , "second" ) ; mustHaveProperty ( actual , "timeZoneName" ) ; mustHaveProperty ( actual , "hour12" ) ;