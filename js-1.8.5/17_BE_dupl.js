
try { 
	var x = [ ] ; 
	x . join = Array . prototype . toString ; 
	"" + x ; 
	throw new Error ( "should have thrown" ) ; 
} catch ( e ) {  } 
try { 
	var x = { 
		toString : Array . prototype . toString , join : Array . prototype . toString 
	} ; 
	"" + x ; 
} 
catch ( e ) {  } 
