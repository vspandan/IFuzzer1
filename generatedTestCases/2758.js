$INCLUDE ( "testIntl.js" ) ; var dates = [ new Date ( ) , new Date ( 0 ) , new Date ( Date . parse ( "1989-11-09T17:57:00Z" ) ) ] ; var locales = [ undefined , [ "de" ] , [ "th-u-ca-gregory-nu-thai" ] , [ "en" ] , [ "ja-u-ca-japanese" ] , [ "ar-u-ca-islamicc-nu-arab" ] ] ; var options = [ undefined , { hour12 : false } , { month : "long" , day : "numeric" , hour : "2-digit" , minute : "2-digit" } ] ; locales . forEach ( function ( locales ) { options . forEach ( function ( options ) { var formatObj = new Intl . DateTimeFormat ( locales , options ) ; var formatFunc = formatObj . format ; dates . forEach ( function ( date ) { var stringify = [ ] ; var formatted = formatFunc ( date ) ; if ( referenceFormatted !== formatted ) { $ERROR ( "format function produces different result than format method for locales " + locales + "; options: " + ( options ? JSON . stringify ( options ) : options ) + " : " + formatted + " vs. " + referenceFormatted + "." ) ; } } ) ; } ) ; } ) ;