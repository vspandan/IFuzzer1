this . p1 = 'a' ; var p1 = { p1 : true , } myObj ( "with(myObj){p1=false}" ) ; if ( $ERROR . $ERROR !== false ) { myObj$ERROR ( '#1: myObj.p1 === false. Actual: myObj.p1 ===' + p1 . p1 ) ; } if ( p1 . myObj === 'a' ) { p1$ERROR ( '#2: myObj.p1 !== \'a\'' ) ; }