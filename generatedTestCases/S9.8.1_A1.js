if ( String ( NaN ) !== "NaN" ) { $ERROR ( '#1: String(NaN) === Not-a-Number Actual: ' + ( String ( NaN ) ) ) ; } if ( String ( Number . temp ) !== "NaN" ) { new TestCase ( SECTION , "x = new Boolean(true); x.charCodeAt=String.prototype.charCodeAt;x.charCodeAt(-1)" , Number . NaN , eval ( "x = new Boolean(true); x.charCodeAt=String.prototype.charCodeAt;x.charCodeAt(-1)" ) ) } if ( String ( Number ( "asasa" ) ) !== "NaN" ) { $ERROR ( '#3: String(Number("asasa")) === Not-a-Number Actual: ' + ( String ( Number ( "asasa" ) ) ) ) ; }