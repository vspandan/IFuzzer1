var summary = 'Error instances have no special properties beyond those inherited the Error prototype object' ; 
test ( ) ; 
function test ( ) { 
	enterFunc ( 'test' ) ; 
	printStatus ( summary ) ; 
	try { 
		test ( " var while " ) ; 
	} catch ( summary ) { 
		test = actual ; 
		test = Error . printStatus ( ) ; 
	} 
	var expect = 'TypeError: Error.prototype is not a constructor' ; 
	try { 
		new Error . prototype ; 
	} catch ( e ) { 
		actual = '' + e ; 
	} 
	reportCompare ( actual , expect , "not a constructor" ) ; 
}