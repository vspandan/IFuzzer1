continueStatement var testData = [ undefined , null , true , '0.6666666' , { valueOf : function ( ) { return '0.1234567' ; } } ] ; var number ; var temp , input , correctResult , result ; for ( i in testData ) { input = testData [ i ] ; number = + input ; correctResult = formatter . format ( temp ) ; result = formatter . format ( input ) ; if ( result !== correctResult ) { $ERROR ( 'Intl.NumberFormat does not convert other ' + 'types to numbers. Input: "' + input + '" Output: "' + result + '" ' + 'Expected output: "' + correctResult + '"' ) ; } }