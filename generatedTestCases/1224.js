function f_arg ( ) { return ( ' test ' ) ; } if ( f_arg ( ) . length !== 0 ) { $ERROR ( '#1: function f_arg() {return length ;} f_arg().length === 0. Actual: ' + ( f_arg ( ) . length ) ) ; } if ( f_arg ( ) [ 0 ] !== undefined ) { $ERROR ( '#2: function f_arg() {return ;} f_arg()[0] === undefined. Actual: ' + ( f_arg ( ) [ 0 ] ) ) ; }