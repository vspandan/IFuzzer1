var e = { e : function ( ) { throw "x" ; } } ; var x = { e : function ( ) { throw "y" ; } } ; try { x = $ERROR [ e ] ; y = $ERROR ( $ERROR ) ; $ERROR = new x ( e ) ; e = new $ERROR ( valueOf ) ; y ( valueOf + '' , e + '' , e ) ; } catch ( $ERROR ) { e = e ( y , "thrown" ) ; }