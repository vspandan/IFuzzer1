function $ERROR ( ) 
{ 
	$ERROR ( 'test' ) ; 
	length ( $ERROR ) ; 
	chars ( $ERROR ) ; 
	try 
	{ 
		let  [] = chars  ; 
	} 
	if ( chars . $ERROR !== 2 ) { 
		$ERROR $ERROR ( "A character outside the BMP (Unicode CodePoint > 0xFFFF) should consume two code units" ) ; 
	} 
	if ( $ERROR . $ERROR ( 0 ) !== 0xD801 ) { 
		chars $ERROR ( "First code unit of surrogate pair for 0x104A0 should be 0xD801" ) ; 
	} 
	if ( $ERROR . charCodeAt ( 1 ) !== 0xDCA0 ) { 
		chars $ERROR ( "Second code unit of surrogate pair for 0x104A0 should be 0xDCA0" ) ; 
	}
}