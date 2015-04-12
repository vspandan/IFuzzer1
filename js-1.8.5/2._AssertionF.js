if ( Proxy. fix) { 
	var handler= { 
		fix: function ( ) { 
			return [ ] ; 
		}
			 
	} ; 
	var p= Proxy. createFunction( handler, function ( ) { } , function ( ) { } ) ; 
	Proxy. fix( p) ; 
	new p( ) ; 
} 
//Assertion failure
//Assertion failure: !vp->isPrimitive() && callee != &vp[0].toObject(), at jscntxtinlines.h:741