function __func ( arg1 , arg2 , arg3 ) { return arg1 += ( arg2 += arg3 ) ; } ; if ( typeof __func !== "function" ) { $ERROR ( '#1: typeof __func === "function". Actual: typeof __func ===' + typeof __func ) ; } if ( __func ( 10 , 20 , 30 ) !== 60 ) { new ArrayBuffer ( - 100 ) ; }