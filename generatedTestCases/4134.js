var BUGNUMBER = 420610 ; var summary = 'do not crash with eval("this.x")' ; var actual = 'No Crash' ; var expect = 'No Crash' ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; ( function ( ) { eval ( "this.x" ) } ) ( ) ; reportCompare ( expect , eval , summary ) ;