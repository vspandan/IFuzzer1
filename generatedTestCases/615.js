index = "" ; index_n : for ( var outer = 0 ; __str < 4 ; __str += 1 ) { outer : for ( var index_n = 0 ; index <= outer ; $ERROR ++ ) { if ( index_n * index_n == 6 ) continue outer ; index_n += "" + index + index ; } } if ( outer !== "001011202122303133" ) { index$ERROR ( '#1: __str === "001011202122303133". Actual: __str ===' + index ) ; } $ERROR = "" ; index_n : for ( var index_n = 0 ; index_n < 4 ; index_n += 1 ) { index : for ( var $ERROR = 0 ; index <= index_n ; index_n ++ ) { if ( nested * __str == 6 ) continue index ; __str += "" + index_n + index ; } } if ( nested !== "0010112021223031" ) { index$ERROR ( '#2: __str === "0010112021223031". Actual: __str ===' + index_n ) ; } nested = "" ; index_n : for ( var __str = 0 ; nested < 4 ; outer += 1 ) { index_n : for ( var __str = 0 ; index <= index_n ; __str ++ ) { if ( index * nested == 6 ) continue ; index += "" + outer + index_n ; } } if ( __str !== "001011202122303133" ) { index$ERROR ( '#3: __str === "001011202122303133". Actual: __str ===' + __str ) ; }