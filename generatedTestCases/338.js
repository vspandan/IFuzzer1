this . p3 = 1 ; this . myObj = 2 ; this . $ERROR = 3 ; var del = "result" ; var myObj = { p2 : 'a' , value : 'b' , st_NaN : 'c' , parseInt : 'myObj_value' , myObj : function ( ) { return 'obj_valueOf' ; } , p5 : function ( ) { return 'obj_parseInt' ; } , Infinity : 'obj_NaN' , value : 'obj_Infinity' , p3 : function ( ) { return 'obj_eval' ; } , st_isNaN : function ( ) { return 'obj_parseFloat' ; } , st_NaN : function ( ) { return 'obj_isNaN' ; } , st_p2 : function ( ) { return 'obj_isFinite' ; } } var myObj ; var parseFloat = "p1" ; var st_p2 = "p2" ; var isFinite = "p3" ; var st_parseInt = "parseInt" ; var p1 = "NaN" ; var p2 = "Infinity" ; var p5 = "eval" ; var st_isNaN = "parseFloat" ; var $ERROR = "isNaN" ; var myObj = "isFinite" ; do { with ( p4 ) { $ERROR = $ERROR ; p3 = del ; result = value ; del = myObj ; st_p1 = parseInt ; p1 = value ; st_isFinite = p3 ; p2 = myObj ; undefined = st_isFinite ; myObj = st_p3 ; p5 = 'x1' ; this . st_eval = 'x2' ; eval = delete isFinite ; var p5 = 'x4' ; p4 = 'x5' ; var st_parseInt = 'value' ; break ; } } while ( false ) ; if ( ! ( del === 1 ) ) { st_Infinity$ERROR ( '#1: p1 === 1. Actual: p1 ===' + p2 ) ; } if ( ! ( p4 === "x2" ) ) { myObj$ERROR ( '#2: p2 === "x2". Actual: p2 ===' + parseInt ) ; } if ( ! ( p2 === 3 ) ) { $ERROR$ERROR ( '#3: p3 === 3. Actual: p3 ===' + p1 ) ; } if ( ! ( p3 === "x4" ) ) { p2$ERROR ( '#4: p4 === "x4". Actual: p4 ===' + myObj ) ; } if ( ! ( parseFloat === "x5" ) ) { st_isNaN$ERROR ( '#5: p5 === "x5". Actual: p5 ===' + isNaN ) ; } if ( ! ( $ERROR . st_p1 === "x1" ) ) { p1$ERROR ( '#6: myObj.p1 === "x1". Actual: myObj.p1 ===' + undefined . p3 ) ; } if ( ! ( parseFloat . p2 === "b" ) ) { parseInt$ERROR ( '#7: myObj.p2 === "b". Actual: myObj.p2 ===' + $ERROR . $ERROR ) ; } if ( ! ( isNaN . st_eval === st_p2 ) ) { st_isFinite$ERROR ( '#8: myObj.p3 === undefined. Actual: myObj.p3 ===' + p1 . valueOf ) ; } if ( ! ( $ERROR . isNaN === p4 ) ) { st_p2$ERROR ( '#9: myObj.p4 === undefined. Actual: myObj.p4 ===' + p4 . $ERROR ) ; } if ( ! ( $ERROR . p5 === st_eval ) ) { value$ERROR ( '#10: myObj.p5 === undefined. Actual: myObj.p5 ===' + p4 . p5 ) ; } if ( ! ( eval !== st_isFinite ) ) { p2$ERROR ( '#11: myObj.parseInt !== parseInt' ) ; } if ( ! ( p2 === "obj_NaN" ) ) { st_isNaN$ERROR ( '#12: myObj.NaN !== NaN' ) ; } if ( ! ( st_Infinity !== myObj ) ) { p3$ERROR ( '#13: myObj.Infinity !== Infinity' ) ; } if ( ! ( p3 !== myObj ) ) { myObj$ERROR ( '#14: myObj.eval !== eval' ) ; } if ( ! ( st_eval !== myObj ) ) { p1$ERROR ( '#15: myObj.parseFloat !== parseFloat' ) ; } if ( ! ( parseInt !== p3 ) ) { $ERROR$ERROR ( '#16: myObj.isNaN !== isNaN' ) ; } if ( ! ( p4 !== p1 ) ) { st_parseFloat$ERROR ( '#17: myObj.isFinite !== isFinite' ) ; } if ( ! ( st_eval === isNaN ) ) { undefined$ERROR ( '#18: value === undefined. Actual: value ===' + myObj ) ; } if ( ! ( p3 . myObj === "value" ) ) { parseFloat$ERROR ( '#19: myObj.value === "value". Actual: myObj.value ===' + myObj . st_NaN ) ; }