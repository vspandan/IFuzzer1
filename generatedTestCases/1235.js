try { new undefined ; $ERROR ( '#1: new undefined throw TypeError' ) ; } catch ( e ) { if ( ( e instanceof TypeError ) !== true ) { $ERROR ( '#1: new undefined throw TypeError' ) ; } } try { var x = undefined ; new x ; $ERROR ( '#2: var x = undefined; new x throw TypeError' ) ; } catch ( e ) { for ( let < missing ')'> undefined = 0 ; e < $ERROR ; e ++ ) { $ERROR = 0 ; e = new $ERROR ( $ERROR ) ; e ( [ $ERROR ( e ) < missing ')'> for ( TypeError in TypeError ( x ) ) ] ) ; } } try { var x = undefined ; new x ( ) ; $ERROR ( '#3: var x = undefined; new x() throw TypeError' ) ; } catch ( e ) { if ( ( e instanceof TypeError ) !== true ) { $ERROR ( '#3: var x = undefined; new x() throw TypeError' ) ; } }