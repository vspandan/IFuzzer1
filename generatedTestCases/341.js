this . p4 = 1 ; this . st_parseFloat = 2 ; this . del = 3 ; var $ERROR = "result" ; var isFinite = { st_NaN : 'a' , NaN : 'b' , st_isNaN : 'c' , p1 : 'myObj_value' , p2 : function ( ) { return 'obj_valueOf' ; } , p3 : function ( ) { return 'obj_parseInt' ; } , $ERROR : 'obj_NaN' , p3 : 'obj_Infinity' , p3 : function ( ) { return 'obj_eval' ; } , st_p1 : function ( ) { return 'obj_parseFloat' ; } , p1 : function ( ) { return 'obj_isNaN' ; } , myObj : function ( ) { return 'obj_isFinite' ; } } var myObj ; var st_eval = "p1" ; var st_isFinite = "p2" ; var st_isNaN = "p3" ; var $ERROR = "parseInt" ; var valueOf = "NaN" ; var myObj = "Infinity" ; var p3 = "eval" ; var myObj = "parseFloat" ; var p1 = "isNaN" ; var p1 = "isFinite" ; with ( p2 ) { var p5 = function ( ) { return st_isFinite ; $ERROR = parseInt ; st_isNaN = myObj ; st_eval = p3 ; myObj = myObj ; f = undefined ; p3 = st_Infinity ; myObj = $ERROR ; p3 = del ; f = st_isFinite ; p5 = myObj ; $ERROR = 'x1' ; this . st_p3 = 'x2' ; parseInt = delete $ERROR ; var st_parseFloat = 'x4' ; st_parseFloat = 'x5' ; var myObj = 'value' ; } var st_parseFloat = new $ERROR ( ) ; } if ( ! ( isFinite === 1 ) ) { st_parseInt$ERROR ( '#1: p1 === 1. Actual: p1 ===' + p4 ) ; } if ( ! ( myObj === 2 ) ) { $ERROR$ERROR ( '#2: p2 === 2. Actual: p2 ===' + $ERROR ) ; } if ( ! ( p3 === 3 ) ) { isNaN$ERROR ( '#3: p3 === 3. Actual: p3 ===' + st_NaN ) ; } try { p2 ; myObj$ERROR ( '#4: p4 is not defined' ) ; } catch ( p3 ) { } try { $ERROR ; st_isFinite$ERROR ( '#5: p5 is not defined' ) ; } catch ( st_p2 ) { } if ( ! ( $ERROR . st_p3 === "a" ) ) { p4$ERROR ( '#6: myObj.p1 === "a". Actual: myObj.p1 ===' + st_isFinite . $ERROR ) ; } if ( ! ( p2 . parseInt === "b" ) ) { st_parseInt$ERROR ( '#7: myObj.p2 === "b". Actual: myObj.p2 ===' + p3 . st_p1 ) ; } if ( ! ( st_eval . $ERROR === "c" ) ) { p3$ERROR ( '#8: myObj.p3 === "c". Actual: myObj.p3 ===' + st_Infinity . valueOf ) ; } if ( ! ( st_isNaN . st_p2 === p2 ) ) { parseFloat$ERROR ( '#9: myObj.p4 === undefined. Actual: myObj.p4 ===' + myObj . st_p1 ) ; } if ( ! ( NaN . st_isNaN === myObj ) ) { p4$ERROR ( '#10: myObj.p5 === undefined. Actual: myObj.p5 ===' + st_parseInt . st_NaN ) ; } if ( ! ( $ERROR === "parseInt" ) ) { $ERROR$ERROR ( '#11: myObj.parseInt === "parseInt". Actual: myObj.parseInt ===' + p2 . obj ) ; } if ( ! ( myObj === "NaN" ) ) { $ERROR$ERROR ( '#12: st_NaN === "NaN". Actual: st_NaN ===' + $ERROR ) ; } if ( ! ( myObj === "Infinity" ) ) { p3$ERROR ( '#13: st_Infinity === "Infinity". Actual: st_Infinity ===' + del ) ; } if ( ! ( st_p3 === "eval" ) ) { st_p1$ERROR ( '#14: st_eval === "eval". Actual: st_eval ===' + p2 ) ; } if ( ! ( st_isNaN === "parseFloat" ) ) { st_isNaN$ERROR ( '#15: st_parseFloat === "parseFloat". Actual: st_parseFloat ===' + result ) ; } if ( ! ( $ERROR === "isNaN" ) ) { myObj$ERROR ( '#16: st_isNaN === "isNaN". Actual: st_isNaN ===' + $ERROR ) ; } if ( ! ( p2 === "isFinite" ) ) { st_Infinity$ERROR ( '#17: st_isFinite === "isFinite". Actual: st_isFinite ===' + isNaN ) ; } try { p3 ; st_NaN$ERROR ( '#18: value is not defined' ) ; } catch ( p1 ) { } if ( ! ( $ERROR . myObj === "myObj_value" ) ) { parseFloat$ERROR ( '#19: myObj.value === "myObj_value". Actual: myObj.value ===' + p3 . p1 ) ; }