var x = Object . preventExtensions ( { } ) ; var y = { } ; try { x . __proto__ = y ; } catch ( err ) { } if ( x . getPrototypeOf ( x ) !== Object . prototype ) { $ERROR ( "Prototype of non-extensible object mutated" ) ; }