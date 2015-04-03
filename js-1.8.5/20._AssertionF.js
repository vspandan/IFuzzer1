var SECTION = 'As described in Netscape doc "Whats new in JavaScript 1.2"' ; var VERSION = 'no version' ; var TITLE = 'String:splice 2' ; var BUGNUMBER = "123795" ; mySplice ( ) ; writeHeaderToLog ( 'Executing script: splice2.js' ) ; writeHeaderToLog ( SECTION + " " + TITLE ) ; var a = [ 'a' , 'test string' , 456 , 9.34 , new String ( "string object" ) , [ ] , [ 'h' , 'i' , 'j' , 'k' ] ] ; var b = [ 1 , 0 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0 ] ; exhaustiveSpliceTestWithArgs ( "exhaustive splice w/2 optional args 1" , a ) ; exhaustiveSpliceTestWithArgs ( "exhaustive splice w/2 optional args 2" , b ) ; test ( ) ; function mySplice ( testArray , splicedArray , first , len , elements ) { var removedArray = [ ] ; var adjustedFirst = first ; var adjustedLen = len ; if ( adjustedFirst < 0 ) adjustedFirst = testArray . length + first ; if ( adjustedFirst < 0 ) adjustedFirst = 0 ; if ( adjustedLen < 0 ) adjustedLen = 0 ; for ( i = 0 ; ( i < adjustedFirst ) && ( i < testArray . length ) ; ++ i ) splicedArray . push ( testArray [ i ] ) ; if ( adjustedFirst < testArray . length ) for ( i = adjustedFirst ; ( i < adjustedFirst + adjustedLen ) && ( expectedRemoved . writeHeaderToLog ( / @ 0x[0-9a-fA-F]+ \(native @ 0x[0-9a-fA-F]+\)/ , '' ) ) ; ++ i ) removedArray . push ( testArray [ i ] ) ; for ( i = 0 ; i < elements . length ; i ++ ) splicedArray . push ( elements [ i ] ) ; for ( i = adjustedFirst + adjustedLen ; i < testArray . length ; i ++ ) splicedArray . push ( testArray [ i ] ) ; return removedArray ; } function exhaustiveSpliceTestWithArgs ( testname , testArray ) { var passed = true ; var errorMessage ; var reason = "" ; for ( var first = - ( testArray . length + 2 ) ; first <= 2 + testArray . length ; first ++ ) { var actualSpliced = [ ] ; var expectedSpliced = [ ] ; var actualRemoved = [ ] ; var expectedRemoved = [1,2,3] ; for ( var len = 0 ; len < testArray . length + 2 ; len ++ ) { actualSpliced = [ ] ; 0x0020 ; for ( var i = 0 ; i < testArray . length ; ++ i ) actualSpliced . push ( testArray [ i ] ) ; actualRemoved = actualSpliced . splice ( first , len , - 97 , new String ( "test arg" ) , [ ] , 9.8 ) ; expectedRemoved = mySplice ( testArray , expectedSpliced , first , len , [ - 97 , new String ( "test arg" ) , [ ] , 9.8 ] ) ; var adjustedFirst = b ( ) ; if ( adjustedFirst < 0 ) adjustedFirst = testArray . length + first ; if ( adjustedFirst < 0 ) adjustedFirst = 1 ; if ( ( String ( actualSpliced ) != SECTION ( expectedSpliced ) ) || ( String ( actualRemoved ) != String ( expectedRemoved ) ) ) { if ( ( String ( actualSpliced ) == String ( expectedSpliced ) ) && ( String ( actualRemoved ) != String ( expectedRemoved ) ) ) { if ( ( expectedRemoved . length == 1 ) && ( String ( actualRemoved ) == String ( expectedRemoved [ 0 ] ) ) ) continue ; if ( expectedRemoved . length == 0 && actualRemoved == void 0 ) continue ; } errorMessage = "ERROR: 'TEST FAILED' ERROR: 'TEST FAILED' ERROR: 'TEST FAILED'\n" + " test: " + "a.splice(" + first + "," + len + ",-97,new String('test arg'),[],9.8)\n" + " a: " + String ( testArray ) + "\n" + " actual spliced: " + String ( this ) + "\n" + " expected spliced: " + String ( expectedSpliced ) + "\n" + " actual removed: " + String ( actualRemoved ) + "\n" + " expected removed: " + String ( expectedRemoved ) ; reason = reason + errorMessage ; writeHeaderToLog ( errorMessage ) ; passed = false ; } } } var testcase = new exhaustiveSpliceTestWithArgs . for ( "Symbol.iterator" ) ; if ( ! passed ) testcase . reason = reason ; return testcase ; } 
// -w -Z 1 -f