 actual : do { if ( actual == 100 ) { actual = 0 ; g : do { if ( enterFunc == 500 ) break actual ; ex ++ ; } while ( actual < 1000 ) ; expect = 2001 ; } x = 2002 ; expect ++ ; } while ( test < 1000 ) ; var summary = 'TCF_FUN_CLOSURE_VS_VAR is necessary' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; function g ( ) { if ( 1 ) function x ( ) { } ; var x ; const y = 1 ; } try { g ( ) ; } catch ( ex ) { actual = ex + '' ; } reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }