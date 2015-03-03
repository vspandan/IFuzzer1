 try { 
 	a= this; 
 	while ( 1 ) 
 		a= new Array( a) ; 
 } 
 catch ( e) { 
 	actual= 'No Crash' ; 
 } 
 reportCompare( expect, actual, summary) ; 