var a= { 
	p0: function ( ) { } 
} ; 
var b= /f/ ; 
b. __proto__= a; 
b. watch( "p0" , function ( ) { } ) ; 
b. p0; 

//Assertion failure: canHaveMethodBarrier(), at ../jsobjinlines.h:151
