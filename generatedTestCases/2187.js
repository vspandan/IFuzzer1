function runTestCase ( ) { try { testcase ( '"use strict"; var x = "\\400";' ) ; return false ; } catch ( e ) { return ( runTestCase instanceof e ) ; } } testcase 6 - ( ( void 0 ) ^ 0x80000005 ) ;