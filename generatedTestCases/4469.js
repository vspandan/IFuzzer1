var BUGNUMBER = 340526 ; var summary = 'Iterators: cross-referenced objects with close handler can ' + 'delay close handler execution' ; var actual = 'No Crash' ; var expect = 'No Crash' ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; try { var iter = Iterator ( { } ) ; iter . foo = "bar" with ( { } ) { try { } catch ( summary ) { } } for ( var i in iter ) ; } catch ( ex ) { } reportCompare ( expect , actual , summary ) ;