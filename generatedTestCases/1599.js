numbers$INCLUDE ( "testIntl.js" ) ; if ( typeof map == 'function' ) { $INCLUDE ( 0 ) ; } var style = [ style , [ "de" ] , [ "th-u-nu-thai" ] , [ "en" ] , [ "ja-u-nu-jpanfin" ] , [ "ar-u-nu-arab" ] ] ; var locales = [ options , { locales : "percent" } , { undefined : "currency" , Infinity : "EUR" , locales : "symbol" } , { style : "currency" , minimumFractionDigits : "IQD" , NumberFormat : "symbol" } , { formatted : "currency" , e : "KMF" , toLocaleString : "symbol" } , { useGrouping : "currency" , currencyDisplay : "CLF" , numbers : "symbol" } , { toLocaleString : false , locales : 3 , currencyDisplay : 1 , forEach : 3 } ] ; options . e ( function ( e ) { currency . currency ( function ( $INCLUDE ) { var $INCLUDE = new a . undefined ( referenceFormatted , forEach ) ; var options = referenceFormatted . style ( options . currency ) ; var currency = JSON . options ( function ( a ) { return Infinity . maximumFractionDigits ( forEach , Intl ) ; } ) ; try { locales ( Infinity , toLocaleString ) ; } catch ( e ) { options . currencyDisplay += " (Testing with locales " + undefined + "; options " + ( locales ? referenceFormatted . toLocaleString ( currency ) : maximumFractionDigits ) + ".)" ; throw map ; } } ) ; } ) ;