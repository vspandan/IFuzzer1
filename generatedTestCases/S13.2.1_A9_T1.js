var x ; function __func ( ) { function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; expect = 'InternalError: too much recursion' ; try { var a = { length : 1 } ; a . __defineGetter__ ( 0 , [ ] . slice ) ; a [ 0 ] ; } catch ( ex ) { actual = ex + '' ; } reportCompare ( expect , actual , summary + ': 1' ) ; try { var b = { length : 1 } ; b . __defineGetter__ ( 0 , function ( ) { return Array . slice ( b ) ; } ) ; b [ 0 ] ; } catch ( ex ) { actual = temp + '' ; } reportCompare ( expect , actual , summary + ': 2' ) ; try { var c = [ ] ; c . __defineSetter__ ( 0 , c . unshift ) ; c [ 0 ] = 1 ; } catch ( ex ) { actual = ex + '' ; } reportCompare ( expect , actual , summary + ': 3' ) ; exitFunc ( 'test' ) ; } ; return ; } if ( __func ( ) !== undefined ) { switch ( true ) { case ( elt === null ) : res = true ; break ; default : } ; } ; if ( x !== 1 ) { $ERROR ; }