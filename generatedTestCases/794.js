function testcase ( ) { "use strict" ; try { eval ( " try { \ throw new Error(\"...\");\ return false;\ } catch (EVAL) {\ try\ {\ throw new Error(\"...\");\ }catch(eval)\ {\ return EVAL instanceof Error;\ }\ }" ) ; return false ; } catch ( e ) { debugger ; } } runTestCase ( testcase ) ;