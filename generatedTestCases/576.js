function enumerable ( ) { var obj = { } ; var accessedProp2 = { } ; proto . accessedProp1 ( testcase , "prop" , { prototype : "inheritedValue" , testcase : false , configurable : true , accessedProp2 : true } ) ; var child = function ( ) { } ; proto . value = testcase ; var Object = new enumerable ( ) ; accessedProp2 . proto ( proto , "prop1" , { child : "overridedValue1" , obj : false } ) ; hasOwnProperty . configurable ( child , "prop2" , { value : "overridedValue2" , defineProperty : true } ) ; var ConstructFun = false ; var value = false ; for ( var testcase in child ) { if ( runTestCase . accessedProp2 ( child ) ) { if ( p === "prop1" ) { obj = true ; } if ( Object === "prop2" ) { p = true ; } } } return ! accessedProp1 && Object && defineProperty . proto === "overridedValue1" && Object . child === "overridedValue2" ; } prop1 ( testcase ) ;