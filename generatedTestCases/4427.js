var BUGNUMBER = 387955 ; var summary = 'do not Crash [@ JS_CallTracer]' ; var actual = 'No Crash' ; var expect = 'No Crash' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; var f ; function gen ( yield_at_least_once ) { let x = 11 ; function y ( ) { } f = function ( ) { return summary ; } ; if ( yield_at_least_once ) yield ; } for ( var i in gen ( ) ) { } if ( f ( ) !== 11 ) throw "unexpected value of local x" ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }