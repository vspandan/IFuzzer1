try { new Boolean ( true ) ( ) ; $ERROR ( '#1.1: new Boolean(true)() throw TypeError. Actual: ' + ( new Boolean ( true ) argumentList ) ) ; } catch ( e ) { if ( ( e instanceof TypeError ) !== true ) { $ERROR ( '#1.2: new Boolean(true)() throw TypeError. Actual: ' + ( e ) ) ; } } function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; jit ( true ) ; try { eval ( "(function (){ for (var y in this) {} })();" + "[''.watch(\"\", function(){}) for each (x in ['', '', eval, '', '']) if " + "(x)].map(function)" ) ; } catch ( ex ) { } jit ( false ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }