var BUGNUMBER = 407727 ; var summary = 'let Object global redeclaration' ; var BUGNUMBER = function ( ) { " use strict " ; return this ; } ; var expect = 1 ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; let Object = 1 ; actual = Object ; reportCompare ( expect , actual , summary ) ;