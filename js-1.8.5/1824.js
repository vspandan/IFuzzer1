var BUGNUMBER = 345967 ; var summary = 'Yet another unrooted atom in jsarray.c' ; 
var actual = '' ; 
var expect = '' ; 
test ( ) ; 
function test ( ) { 
	enterFunc ( 'test' ) ; 
	printBugNumber ( BUGNUMBER ) ; 
	printStatus ( summary ) ; expectExitCode ( 0 ) ; expectExitCode ( 3 ) ; 
	print ( 'this test will probably run out of memory' ) ; 
	print ( 'this test really should only fail on 64 bit machines' ) ; 
	var JSVAL_INT_MAX = ( 1 << 30 ) - 1 ; 
	var a = new Array ( JSVAL_INT_MAX + 15 ) ; 
	a [ JSVAL_INT_MAX ] = 0 ; 
	a [ JSVAL_INT_MAX + 1 ] = 1 ; 
	a . __defineGetter__ ( JSVAL_INT_MAX , function ( ) { 
		return 0 ; 
	} ) ; 
	a . __defineSetter__ ( JSVAL_INT_MAX , 
		function ( value ) { 
			delete a [ JSVAL_INT_MAX + 1 ] ; 
			var tmp = [ ] ; tmp [ JSVAL_INT_MAX + 2 ] = 2 ; 
			if ( typeof gc == 'function' ) 
				gc ( ) ; 
			for ( var i = 0 ; i != 50000 ; ++ i ) { 
				var tmp = 1 / 3 ; tmp /= 10 ; 
			} 
			for ( var i = 0 ; i != 1000 ; ++ i ) { 
				var tmp2 = Array ( 12 ) . join ( ' ' ) ; 
			} 
		} ) ; 
	a . shift ( ) ; 
	expect = 0 ; 
	actual = a [ JSVAL_INT_MAX ] ; 
	if ( expect !== actual ) 
		print ( "BAD" ) ; 
	reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; 
}