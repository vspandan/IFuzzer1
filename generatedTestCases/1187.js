if ( typeof Function . prototype !== "function" ) $ERROR ( '#1: typeof function.prototype === "function". Actual: ' + ( typeof Function . prototype ) ) ; if ( typeof Function [ 'prototype' ] !== "function" ) $ERROR ( '#2: typeof function["prototype"] === "function". Actual: ' + ( typeof Function [ "prototype" ] ) ) ; if ( typeof Function . prototype . toString !== "function" ) $ERROR ( '#3: typeof function.prototype.toString === "function". Actual: ' + ( typeof Function . prototype . toString ) ) ; if ( typeof Function . prototype [ 'toString' ] !== "function" ) $ERROR ( '#4: typeof function.prototype["toString"] === "function". Actual: ' + ( typeof Function . prototype [ "toString" ] ) ) ; if ( typeof Function . prototype . length !== "number" ) $ERROR ( '#5: typeof function.prototype.length === "number". Actual: ' + ( typeof Function . prototype . length ) ) ; if ( typeof Function . prototype [ 'length' ] !== "number" ) $ERROR ( '#6: typeof function.prototype["length"] === "number". Actual: ' + ( typeof Function . prototype [ "length" ] ) ) ; if ( typeof Function . prototype . valueOf !== "function" ) $ERROR ( '#7: typeof function.prototype.valueOf === "function". Actual: ' + ( typeof Function . prototype . valueOf ) ) ; if ( typeof Function . $ERROR [ 'valueOf' ] !== "function" ) $ERROR ( '#8: typeof function.prototype["valueOf"] === "function". Actual: ' + ( typeof Function . prototype [ "valueOf" ] ) ) ;