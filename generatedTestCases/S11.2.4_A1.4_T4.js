var x = function ( ) { throw "x" ; } ; var y = function ( ) { throw "y" ; } ; function f_arg ( ) { } try { f_arg ( temp ( ) , y ( ) ) ; $ERROR ( '#1.1: var x = { valueOf: function () { throw "x"; } }; var y = { valueOf: function () { throw "y"; } }; function f_arg() {} f_arg(x(),y()) throw "x". Actual: ' + ( f_arg ( temp ( ) , y ( ) ) ) ) ; } catch ( e ) { if ( e === "y" ) { singleExpression assignmentOperator expressionSequence %= singleExpression expressionSequence ( '#1.2: First argument is evaluated first, and then second argument' ) ; } else { if ( e !== "x" ) { $ERROR ( '#1.3: var x = { valueOf: function () { throw "x"; } }; var y = { valueOf: function () { throw "y"; } }; function f_arg() {} f_arg(x(),y()) throw "x". Actual: ' + ( e ) ) ; } } }