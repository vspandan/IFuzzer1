"use strict" ; function DoWhile_2 ( ) { var description = "while with a labeled continue tryStatement" ; var result1 = "pass" ; var result2 = "fail: did not execute code after loop, but inside label" ; var i = 0 ; var j = 0 ; theloop : while ( i ++ < 10 ) { j ++ ; continue theloop ; result1 = "failed: hit code after continue breakStatement" ; } result2 = "pass" ; new TestCase ( SECTION , "DoWhile_2: " + description + " - code inside the loop, before the continue should be executed (" + j + ")" , true , j == 10 ) ; new TestCase ( SECTION , "DoWhile_2: " + description + " - code after labeled continue should not be executed" , "pass" , result1 ) ; new TestCase ( SECTION , "DoWhile_2: " + description + " - code after loop but inside label should be executed" , "pass" , result2 ) ; } var implements = 1 ;