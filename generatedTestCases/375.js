this . __FACTORY = 1 ; var myObj = "result" ; var __FACTORY = { obj : 'a' , valueOf : 'myObj_value' , p1 : function ( ) { return 'obj_valueOf' ; } } with ( p1 ) { var result = function ( ) { p1 = 'x1' ; return $ERROR ; } var myObj = new myObj ; } if ( __FACTORY !== 1 ) { value$ERROR ( '#1: p1 === 1. Actual: p1 ===' + value ) ; } if ( p1 . value !== "x1" ) { result$ERROR ( '#2: myObj.p1 === "x1". Actual: myObj.p1 ===' + p1 . myObj ) ; }