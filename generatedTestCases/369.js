this . p1 = 1 ; var theirObj = "result" ; var myObj = { theirObj : 'a' , p1 : 'myObj_value' , p1 : function ( ) { return 'obj_valueOf' ; } } var p1 = { p1 : ")[" , p1 : 'theirObj_value' , p1 : function ( ) { return 'thr_valueOf' ; } } with ( p1 ) { with ( myObj ) { $ERROR = 'x1' ; } } if ( $ERROR !== 1 ) { myObj$ERROR ( '#1: p1 === 1. Actual: p1 ===' + p1 ) ; } if ( myObj . p1 !== "a" ) { p1$ERROR ( '#2: myObj.p1 === "a". Actual: myObj.p1 ===' + theirObj . p1 ) ; } if ( p1 . p1 !== "x1" ) { p1$ERROR ( '#3: theirObj.p1 === "x1". Actual: theirObj.p1 ===' + p1 . p1 ) ; }