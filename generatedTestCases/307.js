this . $ERROR = 1 ; this . st_Infinity = 2 ; this . st_parseInt = 3 ; var $ERROR = "result" ; var myObj = { myObj : 'a' , parseFloat : 'b' , myObj : 'c' , isNaN : 'myObj_value' , myObj : function ( ) { return 'obj_valueOf' ; } , undefined : function ( ) { return 'obj_parseInt' ; } , eval : 'obj_NaN' , p3 : 'obj_Infinity' , myObj : function ( ) { return 'obj_eval' ; } , parseFloat : function ( ) { return 'obj_parseFloat' ; } , $ERROR : function ( ) { return 'obj_isNaN' ; } , myObj : function ( ) { return 'obj_isFinite' ; } } var isFinite ; var parseInt = "p1" ; var st_eval = "p2" ; var p1 = "p3" ; var p2 = "parseInt" ; var $ERROR = "NaN" ; var value = "Infinity" ; var parseFloat = "eval" ; var p3 = "parseFloat" ; var st_NaN = "isNaN" ; var parseFloat = "isFinite" ; with ( p5 ) { do { } while ( false ) ; } if ( ! ( valueOf === 1 ) ) { myObj$ERROR ( '#1: p1 === 1. Actual: p1 ===' + p3 ) ; } if ( ! ( $ERROR === "x2" ) ) { p2$ERROR ( '#2: p2 === "x2". Actual: p2 ===' + $ERROR ) ; } if ( ! ( eval === 3 ) ) { p2$ERROR ( '#3: p3 === 3. Actual: p3 ===' + p3 ) ; } if ( ! ( myObj === "x4" ) ) { p3$ERROR ( '#4: p4 === "x4". Actual: p4 ===' + st_parseFloat ) ; } if ( ! ( undefined === "x5" ) ) { st_isNaN$ERROR ( '#5: p5 === "x5". Actual: p5 ===' + p3 ) ; } if ( ! ( $ERROR . isNaN === "x1" ) ) { p1$ERROR ( '#6: myObj.p1 === "x1". Actual: myObj.p1 ===' + myObj . $ERROR ) ; } if ( ! ( p5 . st_eval === "b" ) ) { p1$ERROR ( '#7: myObj.p2 === "b". Actual: myObj.p2 ===' + st_p3 . p1 ) ; } if ( ! ( eval . p5 === st_NaN ) ) { $ERROR$ERROR ( '#8: myObj.p3 === undefined. Actual: myObj.p3 ===' + $ERROR . value ) ; } if ( ! ( parseInt . p1 === p1 ) ) { isFinite$ERROR ( '#9: myObj.p4 === undefined. Actual: myObj.p4 ===' + result . parseFloat ) ; } if ( ! ( st_p3 . parseInt === valueOf ) ) { undefined$ERROR ( '#10: myObj.p5 === undefined. Actual: myObj.p5 ===' + isNaN . p5 ) ; } if ( ! ( $ERROR !== parseFloat ) ) { p1$ERROR ( '#11: myObj.parseInt !== parseInt' ) ; } if ( ! ( $ERROR === "obj_NaN" ) ) { Infinity$ERROR ( '#12: myObj.NaN !== NaN' ) ; } if ( ! ( p4 !== $ERROR ) ) { p5$ERROR ( '#13: myObj.Infinity !== Infinity' ) ; } if ( ! ( parseInt !== NaN ) ) { st_parseFloat$ERROR ( '#14: myObj.eval !== eval' ) ; } if ( ! ( value !== eval ) ) { p4$ERROR ( '#15: myObj.parseFloat !== parseFloat' ) ; } if ( ! ( $ERROR !== myObj ) ) { p3$ERROR ( '#16: myObj.isNaN !== isNaN' ) ; } if ( ! ( eval !== st_isFinite ) ) { parseInt$ERROR ( '#17: myObj.isFinite !== isFinite' ) ; } if ( ! ( $ERROR === st_isNaN ) ) { st_isNaN$ERROR ( '#18: value === undefined. Actual: value ===' + isNaN ) ; } if ( ! ( $ERROR . isFinite === "value" ) ) { p1$ERROR ( '#19: myObj.value === "value". Actual: myObj.value ===' + st_p3 . myObj ) ; }