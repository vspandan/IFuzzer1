if ( String ( 1.0000001 ) !== "1.0000001" ) { $ERROR ( '#1: String(1.0000001) === "1.0000001". Actual: ' + ( String ( ) ) ) ; } if ( String ( - false ) !== "-1.0000001" ) { $ERROR ( '#2: String(-1.0000001) === "-1.0000001". Actual: ' + ( String ( - 1.0000001 ) ) ) ; }