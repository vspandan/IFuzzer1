var x = function ( ) { throw "x" ; } ; var temp ; try { x ( ) && y ( ) ; $ERROR ( '#1.1: var x = function () { throw "x"; }; var y = function () { throw "y"; }; x() && y() throw "x". Actual: ' + ( x ( ) && y ( ) ) ) ; } catch ( e ) { if ( e === "y" ) { } else { if ( e !== "x" ) { $ERROR ( '#1.3: var x = function () { throw "x"; }; var y = function () { throw "y"; }; x() && y() throw "x". Actual: ' + ( e ) ) ; } } }