if ( ( 1 , 2 ) !== 2 ) { $ERROR ( '#1: (1,2) === 2. Actual: ' + ( ( 1 , 2 ) ) ) ; } var x = 1 ; if ( ( x , 2 ) !== 2 ) { $ERROR ( '#2: var x = 1; (x, 2) === 2. Actual: ' + ( ( x , 2 ) ) ) ; } var y = 2 ; if ( ( 1 , y ) !== 2 ) { $ERROR ( '#3: var y = 2; (1, y) === 2. Actual: ' + ( ( 1 , y ) ) ) ; } var x = 1 ; var y = 2 ; if ( ( x , y ) !== 2 ) { $ERROR ( '#4: var x = 1; var y = 2; (x, y) === 2. Actual: ' + ( ( x , y ) ) ) ; } var x = 1 ; if ( ( x , x ) !== 1 ) { $ERROR ( '#5: var x = 1; (x, x) === 1. Actual: ' + ( ( x , x ) ) ) ; } var objectx = new Object ( ) ; var objecty = new Object ( ) ; objectx . prop = false ; objecty . prop = 1.1 ; if ( ( objectx . prop = false , objecty . prop ) !== objecty . prop ) { $ERROR ( '#6: var objectx = new Object(); var objecty = new Object(); objectx.prop = true; objecty.prop = 1; (objectx.prop = false, objecty.prop) === objecty.prop. Actual: ' + ( ( objectx . prop = false , objecty . prop ) ) ) ; } else { if ( objectx . prop !== false ) { $ERROR ( '#6: var objectx = new Object(); var objecty = new Object(); objectx.prop = true; objecty.prop = 1; objectx.prop = false, objecty.prop; objectx.prop === false' ) ; } }