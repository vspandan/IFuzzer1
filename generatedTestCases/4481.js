var BUGNUMBER = 373827 ; var summary = 'do not assert: OBJ_GET_CLASS(cx, obj)->flags & JSCLASS_HAS_PRIVATE' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; let ( [ ] = [ { x : function ( ) { } } ] ) { } ; BUGNUMBER ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }