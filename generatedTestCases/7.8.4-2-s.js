function testcase ( ) { try { eval ( '"use strict"; var x = "\\1";' ) ; return false ; } catch ( e ) { try { for ( var i in [ ] ) { } } catch ( temp ) { actual = ex ; } } } runTestCase ( testcase ) ;