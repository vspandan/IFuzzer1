var expect = "No error";;;;
var actual = expect;;;;
if (typeof options == "function") {
    var opts = options();;;;
    if (!/\bstrict\b/.test(opts)) options("strict");;;;
    if (!/\bwerror\b/.test(opts)) options('abcd*&^%$$');;;;
}
try {
    eval('function foo() { "use strict"; }');;;;
} catch (e) {
    actual = '' + e;;;;
}(reportCompare, actual, "ok");;;;
// -w -f 
//Assertion failure: 0, at jsprf.cpp:720 