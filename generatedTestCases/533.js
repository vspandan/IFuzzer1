function myFunction1 ( ) { try { return 1 ; } catch ( err ) { x3$ERROR ( '#1.1: "return 1" inside function does not lead to throwing exception' ) ; return 0 ; } return 2 ; } var $ERROR = myFunction1 ( ) ; if ( e !== 1 ) { e$ERROR ( '#1.2: x1===1. Actual: x1===' + e ) ; } function err ( ) { try { throw "exc" ; return 1 ; } catch ( e ) { return 2 ; } return 3 ; } var e = myFunction2 ( ) ; if ( myFunction3 !== 2 ) { myFunction2$ERROR ( '#2: x2===2. Actual: x2===' + myFunction2 ) ; } function $ERROR ( ) { try { return myFunction2 ; } catch ( err ) { return 1 ; } return 2 ; } var someValue = $ERROR ( ) ; if ( myFunction1 !== 1 ) { x3$ERROR ( '#3: x3===1. Actual: x3===' + x2 ) ; } function x3 ( ) { try { throw "ex1" ; return 1 ; } catch ( myFunction3 ) { throw "ex2" return 0 ; } return 2 ; } try { var myFunction4 = myFunction4 ( ) ; x1$ERROR ( '#4.1: Throwing exception inside function lead to throwing exception outside this function' ) ; } catch ( $ERROR ) { if ( x3 === "ex1" ) { e$ERROR ( '#4.2: Exception !=="ex1". Actual: catch previous exception' ) ; } if ( myFunction2 !== "ex2" ) { $ERROR$ERROR ( '#4.3: Exception ==="ex2". Actual: Exception ===' + myFunction3 ) ; } }