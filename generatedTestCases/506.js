try { throw "catchme" ; e$ERROR ( '#1.1: throw "catchme" lead to throwing exception' ) ; } catch ( err ) { if ( delete e ) { e$ERROR ( '#1.2: Exception has DontDelete property' ) ; } if ( $ERROR !== "catchme" ) { e$ERROR ( '#1.3: Exception === "catchme". Actual: Exception ===' + $ERROR ) ; } } try { throw "catchme" ; $ERROR$ERROR ( '#2.1: throw "catchme" lead to throwing exception' ) ; } catch ( e ) { } try { e ; $ERROR$ERROR ( '#2.2: Deleting catching exception after ending "catch" { }' ) ; } catch ( err ) { }