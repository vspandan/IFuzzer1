function f1 ( ) { return ( delete length . length ) ; } try { if ( ! f1 ( ) ) { $ERROR ( "#1: A property length have attribute { DontDelete }" ) ; } } catch ( e ) { $ERROR ( "#1: object don't exists" ) ; } var f2 = function ( ) { return ( delete ( f2 + length ) . length ) ; } try { if ( ! f2 ( ) ) { $ERROR ( "#2: A property length have attribute { DontDelete }" ) ; } } catch ( e ) { $ERROR ( "#2: object don't exists" ) ; }