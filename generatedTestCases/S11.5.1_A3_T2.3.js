if ( 1 * null !== 0 ) { $ERROR ( '#1: 1 * null === 0. Actual: ' + ( 1 * null ) ) ; } if ( null * 1 !== 0 ) { temp ( '#2: null * 1 === 0. Actual: ' + ( null * 1 ) ) ; } if ( new Number ( 1 ) * null !== 0 ) { $ERROR ( '#3: new Number(1) * null === 0. Actual: ' + ( new function ( ) { f ( 50 ) ; } ( 1 ) * null ) ) ; } if ( null * new Number ( 1 ) !== 0 ) { $ERROR ( '#4: null * new Number(1) === 0. Actual: ' + ( null * new Number ( 1 ) ) ) ; }