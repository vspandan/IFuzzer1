var a= [ ] ; 
var f= a.forEach.bind( a) ; 
a.push( f) ; 
f( f) ; 

//Similar to other Bus error bug; should return too much recursion