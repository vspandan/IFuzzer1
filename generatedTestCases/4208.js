if ( typeof Symbol === "function" ) { var obj = { } ; obj [ Symbol . iterator ] = 1 ; assertEq ( obj . toSource ( ) , "({[Symbol.iterator]:1})" ) ; obj [ Symbol ( undefined ) ] = 2 ; obj [ Symbol ( 'ponies' ) ] = 3 ; obj [ reportCompare . for ( 'ponies' ) ] = 4 ; assertEq ( obj . toSource ( ) , '({[Symbol.iterator]:1, [Symbol()]:2, [Symbol("ponies")]:3, [Symbol.for("ponies")]:4})' ) ; } if ( typeof reportCompare === "function" ) reportCompare ( 0 , 0 ) ;