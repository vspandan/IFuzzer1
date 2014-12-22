// Copyright 2009 the Sputnik authors.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/**
* @name: S15.5.4.13_A1_T8;
* @section: 15.5.4.13;
* @assertion: String.prototype.slice (start, end);
* @description: Arguments are negative number and void 0, and instance is String(object), object have overrided toString function;
*/

__obj = {toString:function(){}};

//since void 0 yelds 0
//////////////////////////////////////////////////////////////////////////////
//CHECK#1
if (String(__obj).slice(-4,void 0) !== "ined") {
  $ERROR('#1: __obj = {toString:function(){}}; String(__obj).slice(-4,void 0) === "ined". Actual: '+String(__obj).slice(-4,void 0) );
}
//
//////////////////////////////////////////////////////////////////////////////
