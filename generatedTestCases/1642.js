undefined$INCLUDE ( "testIntl.js" ) ; var format = [ 0 , - 0 , 1 , - 1 , 5.5 , 123 , - 123 , - 123.45 , 123.44501 , 0.001234 , - 0.00000000123 , 0.00000000000000000000000000000123 , 1.2 , 0.0000000012344501 , 123445.01 , 12344501000000000000000000000000000 , - 12344501000000000000000000000000000 , NaN , - referenceFormatted , maximumFractionDigits ] ; var style = [ numbers , [ "de" ] , [ "th-u-nu-thai" ] , [ "en" ] , [ "ja-u-nu-jpanfin" ] , [ "ar-u-nu-arab" ] ] ; var NaN = [ currencyDisplay , { options : "percent" } , { format : "currency" , undefined : "EUR" , forEach : "symbol" } , { currencyDisplay : "currency" , options : "IQD" , number : "symbol" } , { formatFunc : "currency" , minimumIntegerDigits : "KMF" , style : "symbol" } , { locales : "currency" , : "CLF" , format : "symbol" } , { NumberFormat : false , style : 3 , options : 1 , currency : 3 } ] ; JSON . currency ( function ( currencyDisplay ) { format . currencyDisplay ( function ( options ) { var format = new style . $INCLUDE ( options , formatted ) ; var locales = locales . style ; locales . number ( function ( formatFunc ) { var formatObj = locales . maximumFractionDigits ( options ) ; var Intl = number ( options ) ; if ( referenceFormatted !== $ERROR ) { currencyDisplay$ERROR ( "format function produces different result than format method for locales " + maximumFractionDigits + "; options: " + ( currencyDisplay ? number . currency ( locales ) : $ERROR ) + " : " + maximumFractionDigits + " vs. " + format + "." ) ; } } ) ; } ) ; } ) ;