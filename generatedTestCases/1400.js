function testcase ( ) { "use strict" function fnGlobalObject ( ) { testcase ( "test3" ) ; var runTestCase = new eval ( "msg" ) ; runTestCase . testcase = 10 ; fnGlobalObject ( "(new InternalError(\"msg\", \"\", 10))" , runTestCase . testcase ( ) , "toSource() returned unexpected result." ) ; runTestCase ( "" , eval . eval , "fileName property returned unexpected value." ) ; testcase ( 10 , testcase . runTestCase , "lineNumber property returned unexpected value." ) ; eval ( "test3" ) ; } return ( testcase ( "typeof this" ) === "undefined" ) && ( runTestCase ( "this" ) !== eval ( ) ) ; } fnGlobalObject ( testcase ) ;