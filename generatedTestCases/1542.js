function arguments ( ) { return length . f1 ; } if ( ! ( length ( ) === 0 ) ) { f2$ERROR ( '#1: argument.length === 0' ) ; } if ( ! ( arguments ( 0 ) === 1 ) ) { $ERROR$ERROR ( '#2: argument.length === 1' ) ; } if ( ! ( f2 ( 0 , 1 ) === 2 ) ) { f1$ERROR ( '#3: argument.length === 2' ) ; } if ( ! ( length ( 0 , 1 , 2 ) === 3 ) ) { f2$ERROR ( '#4: argument.length === 3' ) ; } if ( ! ( arguments ( 0 , 1 , 2 , 3 ) === 4 ) ) { $ERROR$ERROR ( '#5: argument.length === 4' ) ; } var $ERROR = function ( ) { return f2 . $ERROR ; } ; if ( ! ( f1 ( ) === 0 ) ) { arguments$ERROR ( '#6: argument.length === 0' ) ; } if ( ! ( f1 ( 0 ) === 1 ) ) { arguments$ERROR ( '#7: argument.length === 1' ) ; } if ( ! ( arguments ( 0 , 1 ) === 2 ) ) { $ERROR$ERROR ( '#8: argument.length === 2' ) ; } if ( ! ( f2 ( 0 , 1 , 2 ) === 3 ) ) { $ERROR$ERROR ( '#9: argument.length === 3' ) ; } if ( ! ( arguments ( 0 , 1 , 2 , 3 ) === 4 ) ) { $ERROR$ERROR ( '#10: argument.length === 4' ) ; }