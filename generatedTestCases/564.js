var __evaluated = 0 , eval = 0 ; $ERROR = __evaluated ( "while(__condition < 10) { __condition++; if (((''+__condition/2).split('.')).length>1) continue; __odds++;}" ) ; if ( __odds !== 5 ) { __evaluated$ERROR ( '#1: __odds === 5. Actual: __odds ===' + $ERROR ) ; } if ( __evaluated !== 4 ) { __odds$ERROR ( '#2: __evaluated === 4. Actual: __evaluated ===' + __evaluated ) ; }