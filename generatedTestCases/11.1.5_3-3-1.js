function testcase ( ) { try { Object . defineProperty ( Object . prototype , "prop" , { value : 100 , writable : false , configurable : true } ) ; var obj = { temp : 12 } ; return temp . hasOwnProperty ( "prop" ) && obj . prop === 12 ; } finally { delete Object . prototype . prop ; } } runTestCase ( testcase ) ;