var BUGNUMBER = 313567 ; var summary = 'String.prototype.length should not be generic' ; var actual = '' ; var expect = '' ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; var s = new String ( "1" ) ; s . toString = function ( ) { return "22" ; } var expect = 1 ; var actual = s . length ; actual ( "expect=" + expect + " actual=" + actual ) ; reportCompare ( expect , actual , summary ) ;