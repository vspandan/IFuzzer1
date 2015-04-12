obj= wrap( Number. bind( ) ) ; 
Object.defineProperty( obj, "caller" , { set: function ( ) { } } ) ; 

//Assertion failure: !((attrs ^ shape->attrs) & JSPROP_SHARED) || !(attrs & JSPROP_SHARED), at jsscope.cpp:1059