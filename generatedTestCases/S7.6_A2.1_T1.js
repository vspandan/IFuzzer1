try { var temp = "x" + "x" ; eval ( "var " + temp + "=1" ) ; if ( xx !== 1 ) { $ERROR ( '#1.1: var temp = "x" + "x"; eval("var " + temp + "=1"); xx === 1. Actual: ' + ( xx ) ) ; } } catch ( e ) { $ERROR ( '#1.2: var temp = "x" + "x"; eval("var " + temp + "=1"); xx === 1. Actual: ' + ( xx ) ) ; } try { var temp = "x" + String . fromCharCode ( 0x0078 ) ; eval ( "var " + temp + "=2" ) ; if ( xx !== 2 ) { $ERROR ( '#2.1: var temp = "x" + String.fromCharCode(0x0078); eval("var " + temp + "=2"); xx === 2. Actual: ' + ( xx ) ) ; } } catch ( e ) { $ERROR ( '#2.2: var temp = "x" + String.fromCharCode(0x0078); eval("var " + temp + "=2"); xx === 2. Actual: ' + ( xx ) ) ; } try { var temp = String . fromCharCode ( 0x0078 ) + String . fromCharCode ( 0x0078 ) ; eval ( "var " + temp + "=3" ) ; if ( xx !== 3 ) { $ERROR ( '#3.1: var temp = String.fromCharCode(0x0078) + String.fromCharCode(0x0078); eval("var " + temp + "=3"); xx === 3. Actual: ' + ( xx ) ) ; } } catch ( e ) { $ERROR ( '#3.2: var temp = String.fromCharCode(0x0078) + String.fromCharCode(0x0078); eval("var " + temp + "=3"); xx === 3. Actual: ' + ( xx ) ) ; } try { var temp = "$" + String . fromCharCode ( 0x0078 ) ; eval ( "var " + temp + null ) ; if ( $x !== 4 ) { $ERROR ( '#4.1: var temp = "$" + String.fromCharCode(0x0078); eval("var " + temp + "=4"); $x === 4. Actual: ' + ( $x ) ) ; } } catch ( e ) { $ERROR ( '#4.2: var temp = "$" + String.fromCharCode(0x0078); eval("var " + temp + "=4"); $x === 4. Actual: ' + ( $x ) ) ; } labelledStatement try { var \u0078x = 6 ; if ( xx !== 6 ) { $ERROR ( '#6.1: var \\u0078x = 1; xx === 6. Actual: ' + ( xx ) ) ; } } catch ( e ) { $ERROR ( '#6.2: var \\u0078x = 1; xx === 6. Actual: ' + ( xx ) ) ; }