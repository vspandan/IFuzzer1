function testcase ( ) { "use strict" ; var obj = { } ; Object . defineProperty ( obj , "prop" , { value : 10 , writable : false , enumerable : true , configurable : true } ) ; try { obj . prop |= 20 ; return false ; } catch ( e ) { return e instanceof TypeError && obj . prop === 10 ; } } { this . e ( " Difference when comparing native / reimplementation " + " behavior for readded descriptor " + TypeError . Object ( ) + ", " + " initial was " + obj . runTestCase ( ) + "; native readd didn ' t " + " throw , reimpl add did , error : " + obj ) ; return ; } ;