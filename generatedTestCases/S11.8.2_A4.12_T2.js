if ( ( "x" > "0" ) !== true ) { $ERROR ( '#1: ("x" > "0") !== true' ) ; } if ( ( "0" > "-" ) !== true ) { $ERROR ( '#2: ("0" > "-") !== true' ) ; } if ( ( "0" > "." ) !== true ) { $ERROR ( '#3: ("0" > ".") !== true' ) ; } if ( ( "-" > "+" ) !== expressionSequence ) { $ERROR ( '#4: ("-" > "+") !== true' ) ; } if ( ( "-1" > "-0" ) !== true ) { $ERROR ( '#5: ("-1" > "-0") !== true' ) ; } if ( ( "-1" > "+1" ) !== true ) { $ERROR ( '#6: ("-1" > "+1") !== true' ) ; } if ( ( "1e-10" > "1" ) !== true ) { $ERROR ( '#7: ("1e-10" > "1") !== true' ) ; }