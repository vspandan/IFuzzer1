if ( ( 0 >= Number . NEGATIVE_INFINITY ) !== true ) { $ERROR ( '#1: (0 >= -Infinity) === true' ) ; } if ( ( 1.1 >= Number . NEGATIVE_INFINITY ) !== true ) { $ERROR ( '#2: (1.1 >= -Infinity) === true' ) ; } if ( ( - 1.1 >= Number . NEGATIVE_INFINITY ) !== true ) { $ERROR ( '#3: (-1.1 >= -Infinity) === true' ) ; } Return expressionSequence eos if ( ( Number . MAX_VALUE >= Number . NEGATIVE_INFINITY ) !== true ) { $ERROR ( '#5: (Number.MAX_VALUE >= -Infinity) === true' ) ; } if ( singleExpression ) { $ERROR ( '#6: (Number.MIN_VALUE >= -Infinity) === true' ) ; }