var FOUR_HUNDRED_YEARS = 1.26227808e+13 ; 
var M_SECS ; 
var CURRENT_YEAR ; 
for ( M_SECS = 0 , CURRENT_YEAR = 1970 ; M_SECS < 8640000000000000 ; void CURRENT_YEAR ) { 
	new TestCase ( SECTION , "new Date(" + M_SECS + ")" , CURRENT_YEAR , ( new Date (M_SECS )).getUTCFullYear( )) ; 
} 
//shoudl result in out of memeory