this . p3 = 1 ; this . parseInt = 2 ; this . myObj = 3 ; var parseFloat = "result" ; var p3 = { p3 : 'a' , myObj : 'b' , p3 : 'c' , p1 : 'myObj_value' , $ERROR : function ( ) { return 'obj_valueOf' ; } , p5 : function ( ) { return 'obj_parseInt' ; } , del : 'obj_NaN' , p1 : 'obj_Infinity' , $ERROR : function ( ) { return 'obj_eval' ; } , st_parseInt : function ( ) { return 'obj_parseFloat' ; } , p4 : function ( ) { return 'obj_isNaN' ; } , $ERROR : function ( ) { return 'obj_isFinite' ; } } var st_isNaN ; var st_p3 = "p1" ; var st_isNaN = "p2" ; var undefined = "p3" ; var p3 = "parseInt" ; var f = "NaN" ; var p2 = "Infinity" ; var Infinity = "eval" ; var $ERROR = "parseFloat" ; var isNaN = "isNaN" ; var isFinite = "isFinite" ; with ( st_isFinite ) { var parseInt = function ( ) { $ERROR = myObj ; p5 = st_parseInt ; p4 = st_isNaN ; p2 = p5 ; myObj = st_p1 ; undefined = p2 ; p5 = myObj ; st_Infinity = undefined ; p3 = $ERROR ; p3 = myObj ; myObj = 'x1' ; this . myObj = 'x2' ; valueOf = delete p5 ; var $ERROR = 'x4' ; st_NaN = 'x5' ; var p3 = 'value' ; return p1 ; } parseInt = value ( ) ; } if ( ! ( $ERROR === "value" ) ) { myObj$ERROR ( '#0: result === "value". Actual: result ===' + $ERROR ) ; } if ( ! ( eval === 1 ) ) { myObj$ERROR ( '#1: p1 === 1. Actual: p1 ===' + $ERROR ) ; } if ( ! ( value === "x2" ) ) { undefined$ERROR ( '#2: p2 === "x2". Actual: p2 ===' + myObj ) ; } if ( ! ( $ERROR === 3 ) ) { myObj$ERROR ( '#3: p3 === 3. Actual: p3 ===' + $ERROR ) ; } try { Infinity ; eval$ERROR ( '#4: p4 is not defined' ) ; } catch ( parseInt ) { } if ( ! ( p2 === "x5" ) ) { p2$ERROR ( '#5: p5 === "x5". Actual: p5 ===' + NaN ) ; } if ( ! ( del . p2 === "x1" ) ) { p1$ERROR ( '#6: myObj.p1 === "x1". Actual: myObj.p1 ===' + myObj . myObj ) ; } if ( ! ( st_p2 . st_p3 === "b" ) ) { value$ERROR ( '#7: myObj.p2 === "b". Actual: myObj.p2 ===' + p2 . value ) ; } if ( ! ( parseFloat . parseInt === result ) ) { st_NaN$ERROR ( '#8: myObj.p3 === undefined. Actual: myObj.p3 ===' + p2 . Infinity ) ; } if ( ! ( myObj . $ERROR === value ) ) { p3$ERROR ( '#9: myObj.p4 === undefined. Actual: myObj.p4 ===' + st_Infinity . undefined ) ; } if ( ! ( st_eval . parseInt === st_p1 ) ) { del$ERROR ( '#10: myObj.p5 === undefined. Actual: myObj.p5 ===' + e . st_eval ) ; } if ( ! ( Infinity !== NaN ) ) { $ERROR$ERROR ( '#11: myObj.parseInt !== parseInt' ) ; } if ( ! ( del === "obj_NaN" ) ) { f$ERROR ( '#12: myObj.NaN !== NaN' ) ; } if ( ! ( p3 !== p1 ) ) { undefined$ERROR ( '#13: myObj.Infinity !== Infinity' ) ; } if ( ! ( NaN !== p4 ) ) { st_parseInt$ERROR ( '#14: myObj.eval !== eval' ) ; } if ( ! ( value !== isNaN ) ) { st_isFinite$ERROR ( '#15: myObj.parseFloat !== parseFloat' ) ; } if ( ! ( $ERROR !== eval ) ) { p3$ERROR ( '#16: myObj.isNaN !== isNaN' ) ; } if ( ! ( st_NaN !== $ERROR ) ) { st_p2$ERROR ( '#17: myObj.isFinite !== isFinite' ) ; } try { myObj ; $ERROR$ERROR ( '#18: value is not defined' ) ; } catch ( $ERROR ) { } if ( ! ( myObj ( typeof myObj , "function" ) === "myObj_value" ) ) { value$ERROR ( '#19: myObj.value === "myObj_value". Actual: myObj.value ===' + value . myObj ) ; }