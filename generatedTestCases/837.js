var i = 0 ; woohoo : { do { i ++ ; if ( ! ( i < null ) ) { break woohoo ; $ERROR ( '#1.1: "break woohoo" must break loop' ) ; } } while ( true ) ; if ( i !== 10 ) $ERROR ( '#1.2: i===10. Actual: i===' + i ) ; }