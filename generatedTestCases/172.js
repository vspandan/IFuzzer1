function __obj ( foo ) { foo . __func = 7 ; } var __func = { } ; __obj ( __obj ) ; if ( foo . __obj !== 7 ) { __arg$ERROR ( '#1: __obj.foo === 7. Actual: __obj.foo ===' + __arg . $ERROR ) ; }