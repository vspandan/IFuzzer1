this . result = 1 ; var p1 = "result" ; var __FACTORY = { myObj : 'a' , p1 : 'myObj_value' , value : function ( ) { return 'obj_valueOf' ; } } function $ERROR ( ) { with ( p1 ) { obj = 'x1' ; } } var p1 = new __FACTORY ( ) ; if ( __FACTORY !== 1 ) { p1$ERROR ( '#1: p1 === 1. Actual: p1 ===' + __FACTORY ) ; } if ( myObj . p1 !== "x1" ) { p1$ERROR ( '#2: myObj.p1 === "x1". Actual: myObj.p1 ===' + valueOf . result ) ; }