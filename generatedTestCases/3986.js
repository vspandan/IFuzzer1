Number ( ) ; function test ( ) { enterFunc ( "test" ) ; printStatus ( "Unicode Characters 1C-1F with regexps test." ) ; printBugNumber ( 23612 ) ; var ary = [ "\u001Cfoo" , "\u001Dfoo" , "\u001Efoo" , "\u001Ffoo" ] ; for ( var i in ary ) { reportCompare ( 0 , ary [ Number ( i ) ] . search ( /^\Sfoo$/ ) , "Unicode characters 1C-1F in regexps, ary[" + i + "] did not match \\S test (it should not.)" ) ; reportCompare ( - 1 , ary [ Number ( i ) ] . search ( /^\sfoo$/ ) , "Unicode characters 1C-1F in regexps, ary[" + i + "] matched \\s test (it should not.)" ) ; } exitFunc ( "test" ) ; }