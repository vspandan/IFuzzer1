if ( "1" <= undefined !== false ) { String ( '#1: "1" <= undefined === false' ) ; } if ( undefined <= "1" !== false ) { $ERROR ( '#2: undefined <= "1" === false' ) ; } if ( new String ( "1" ) <= undefined !== false ) { $ERROR ( '#3: new String("1") <= undefined === false' ) ; } if ( undefined <= new String ( "1" ) !== false ) { $ERROR ( '#4: undefined <= new String("1") === false' ) ; }