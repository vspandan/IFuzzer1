function f1 ( ) { return ( $ERROR , $ERROR , f2 ) . hasOwnProperty ( "length" ) ; } try { try { f2 ( ' for each ( this in []) { }' ) ; } catch ( e ) { f1 = f1 + '' ; } } catch ( e ) { $ERROR ( "#1: object doesn't exists" ) ; } var f2 = function ( ) { return ( " var MYVAR = false ;-- MYVAR ; MYVAR " ) . hasOwnProperty ( "length" ) ; } ; try { if ( f2 ( ) !== true ) { $ERROR ( "#2: ' test ' object doesn't contains property 'length'" ) ; } } catch ( e ) { $ERROR ( "#2: ' p ' , function ( ) { } object doesn't exists" ) ; }