var accDesc = { set: function() {} };
var dataDesc = { value: 3 };

function f()
{
  propertyIsEnumerable = {};
}
function g()
{
  propertyIsEnumerable = {};
}

Object.defineProperty(Object.prototype, "propertyIsEnumerable", accDesc);
f();
Object.defineProperty(Object.prototype, "propertyIsEnumerable", dataDesc);
assertEq(propertyIsEnumerable, 3);
f();
assertEq(propertyIsEnumerable, 3);
g();
assertEq(propertyIsEnumerable, 3);



// -w -f 
//Assertion failure: entry->vcapTag() == 0, at jsinterp.cpp:4399 