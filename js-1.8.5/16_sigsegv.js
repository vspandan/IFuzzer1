assertRaises( StopIteration, function ( ) { 
	Iterator. prototype. next( ) ; Iterator. prototype. next( ) ; 
} ) ; 
assertRaises( StopIteration, function ( ) { 
	Iterator. prototype. next( ) ; 
} ) ; 
assertRaises( StopIteration, function ( ) { 
	( new Iterator( { } ) ).__proto__. next( ) ; 
} ) ; 
function assertRaises( exc, callback) { 
	try { 
		callback( ) ; 
	} catch ( e) { 
	} 
}
