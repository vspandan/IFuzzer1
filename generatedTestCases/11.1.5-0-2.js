function testcase ( ) { var s1 = "First getter" ; var identifier initialiser , variableDeclaration , variableDeclarationList ; var s3 = "Second getter" ; eval ( "var o = {get foo(){ return s1;},set foo(arg){return s2 = s3}, get bar(){ return s3}, set bar(arg){ s3 = arg;}};" ) ; if ( typeof SECTION , "value = 0; for ( ob[\"0\"] in o ) { result += o[o[\"0\"]]" , 6 , result ) return true ; o . foo = singleExpression ; if ( s2 !== s3 ) return false ; if ( o . bar !== s3 ) return false ; o . bar = "Second setter" ; if ( o . bar !== "Second setter" ) return false ; return true ; } runTestCase ( testcase ) ;