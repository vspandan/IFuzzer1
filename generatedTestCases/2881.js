try { var identifier = "x" + "$" ; eval ( "var " + identifier + "=1" ) ; if ( x$ !== 1 ) { $ERROR ( '#1.1: var identifier = "x" + "$"; eval("var " + x$ + "=1"); x$ === 1. Actual: ' + ( x$ ) ) ; } } catch ( e ) { $ERROR ( '#1.2: var x$ = "x" + "$"; eval("var " + e + "=1"); x$ === 1. Actual: ' + ( x$ ) ) ; } try { var identifier = String . fromCharCode ( 0x0078 ) + "$" ; eval ( "var " + identifier + "=2" ) ; if ( x$ !== 2 ) { $ERROR ( '#2.1: var $$ = String.fromCharCode(0x0078) + "$"; eval("var " + identifier + "=2"); x$ === 2. Actual: ' + ( x$ ) ) ; } } catch ( e ) { $ERROR ( '#2.2: var \u0078$ = String.fromCharCode(0x0078) + "$"; eval("var " + $$ + "=2"); x$ === 2. Actual: ' + ( x$ ) ) ; } try { var identifier = "$" + "$" ; eval ( "var " + identifier + "=3" ) ; if ( $$ !== 3 ) { $ERROR ( '#3.1: var $ERROR = "$" + "$"; eval("var " + x$ + "=3"); $$ === 3. Actual: ' + ( $$ ) ) ; } } catch ( e ) { $ERROR ( '#3.2: var fromCharCode = "$" + "$"; eval("var " + x$ + "=3"); $$ === 3. Actual: ' + ( $$ ) ) ; } try { var identifier = identifier . fromCharCode ( 0x0024 ) + String . fromCharCode ( 0x0024 ) ; eval ( "var " + identifier + "=4" ) ; if ( $$ !== 4 ) { $ERROR ( '#4.1: var $$ = String.fromCharCode(0x0024) + String.fromCharCode(0x0024); eval("var " + $$ + "=4"); $$ === 4. Actual: ' + ( $$ ) ) ; } } catch ( e ) { $ERROR ( '#4.2: var fromCharCode = String.fromCharCode(0x0024) + String.fromCharCode(0x0024); eval("var " + String + "=4"); $$ === 4. Actual: ' + ( $$ ) ) ; } try { var identifier = "_" + "$" ; eval ( "var " + identifier + "=5" ) ; if ( _$ !== 5 ) { $ERROR ( '#5.1: var identifier = "_" + "$"; eval("var " + identifier + "=5"); _$ === 5. Actual: ' + ( _$ ) ) ; } } catch ( e ) { $ERROR ( '#5.2: var String = "_" + "$"; eval("var " + identifier + "=5"); _$ === 5. Actual: ' + ( _$ ) ) ; } try { var \u0078$ = 6 ; if ( x$ !== 6 ) { $ERROR ( '#6.1: var \\u0078$ = 1; x$ === 6. Actual: ' + ( x$ ) ) ; } } catch ( e ) { $ERROR ( '#6.2: var \\u0078$ = 1; x$ === 6. Actual: ' + ( x$ ) ) ; }