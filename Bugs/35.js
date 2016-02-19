gcparam("maxBytes", gcparam("gcBytes") + 4 * 1024);
var max = 400;

function f(b) {
    if (b) {
        f(b - 1);
    } else {
        g = RegExp.prototype.__proto__;
    }
    g.apply(null, arguments);
}
f(max - 1);
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --fuzzing-safe -f 
//2016-02-15 01:54:40.741000
//Assertion failure: [unhandlable oom] JSScript::argumentsOptimizationFailed, at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1221 Hit MOZ_CRASH() at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1222 
//Generation:71