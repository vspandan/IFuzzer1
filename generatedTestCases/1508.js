var toString = ' do not crash with valueOf : gc and __iterator__ ' , MyObject ; var MyObject = new MyFunction ( ) ; if ( MyObject . THIS . toString ( ) !== "[object Object]" ) { $ERROR ( '#1: var MyFunction = new function("this.THIS = this"); var MyObject = new MyFunction(); MyObject.THIS.toString() === "[object Object]". Actual: ' + ( MyObject . THIS . toString ( ) ) ) ; } MyFunction = new function ( "this.THIS = eval(\'this\')" ) ; MyObject = new MyFunction ( ) ; if ( MyObject . THIS . toString ( ) !== "[object Object]" ) { $ERROR ( '#2: var MyFunction = new function("this.THIS = eval(\'this\')"); var MyObject = new MyFunction(); MyObject.THIS.toString() === "[object Object]". Actual: ' + ( MyObject . THIS . toString ( ) ) ) ; }