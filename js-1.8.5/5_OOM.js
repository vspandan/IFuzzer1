function inRhino()
{
  return (typeof defineClass == "function");
}
var IN_RHINO= inRhino( ) ; 
try { 
	if ( ! IN_RHINO) { 
		var a1= Array( 0xFFFFFFFF ) ; 
		a1. sort( ) ; 
		a1= null ; 
	} 
	var a2= Array( 0x40000000 ) ; 
	a2. sort( ) ; 
	a2= null ; 
	var a3= Array( 0x10000000 / 4 ) ; 
	a3. sort( ) ; 
	a3= null ; 
} 
catch ( ex) { 
	expect= 'InternalError: allocation size overflow' ; 
	actual= ex+ '' ; 
} 