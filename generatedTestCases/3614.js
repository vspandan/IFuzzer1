var SECTION = "LexicalConventions/regexp-literals-001.js" ; var VERSION = "ECMA_2" ; var TITLE = "Regular Expression Literals" ; startTest ( ) ; s = "passed" ; AddTestCase ( "// should be a comment, not a regular expression null" , "passed" , String ( s ) ) ; AddTestCase ( "// typeof object should be type of object declared on following line" , "passed" , ( typeof s ) == "string" ? "passed" : "failed" ) ; String : : ; test ( ) ;