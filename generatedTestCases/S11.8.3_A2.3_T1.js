var x = { temp : function ( ) { throw "x" ; } } ; var y = { valueOf : function ( ) { assertEq ( "123" . indexOf ( "" , 3 ) , 3 ) } } ; try { x <= y ; $ERROR ( '#1.1: Should have thrown' ) ; } catch ( e ) { if ( e === "y" ) { new TestCase ( SECTION , "var arr=new Array(); arr[Math.pow(2,30)] = 'hi'; arr.length" , Math . pow ( 2 , 30 ) + 1 , eval ( "var arr=new Array(); arr[Math.pow(2,30)] = 'hi'; arr.length" ) ) ; } else { if ( e !== "x" ) { $ERROR ( '#1.3: Failed with: ' + e ) ; } } }