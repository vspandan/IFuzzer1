var gTestfile = 'regress-580544.js' ; var BUGNUMBER = 580544 ; var summary = 'do not assert: new (this.prototype = this)' ; var actual = 'No Crash' ; var expect = 'No Crash' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; try { new ( this . prototype = this ) ; } catch ( e ) { } exitFunc ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }