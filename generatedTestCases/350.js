function __func ( ) { var x = true ; return x ; } try { x = x ; $ERROR ( true ) ; } catch ( e ) { if ( e instanceof Test262Error ) throw e ; } try { var __x = __func ( ) } catch ( e ) { $ERROR ( '#1: var __x=__func() does not lead to throwing exception. Actual: exception is ' + e ) ; } if ( ! ( __x ) ) { $ERROR ( '#2: __x === true. Actual: __x ===' + __x ) ; } try { x = x ; $ERROR ( '#3: "x=x" lead to throwing exception' ) ; } catch ( e ) { if ( e instanceof Test262Error ) throw e ; }