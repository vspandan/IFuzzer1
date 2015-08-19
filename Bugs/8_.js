var isConstructing = getSelfHostedValue("_IsConstructing");

function testBasic() {
    var f = function(expected) {
        with(this) {};
        assertEq(isConstructing(), expected);
    };
    for (var i = 0; i < 40; i++) {
        f(false);
        new f(true);
    }
}
testBasic();

function testGeneric() {
    var f1 = function(expected) {
        with(this) {};
        assertEq(isConstructing(), expected);
    };
    var f2 = function(expected) {
        assertEq("\u2029" + "var" + "\u2029" + "x" + "\u2029" + "=" + "\u2029" + "2" + "\u2029; result = x;", expected);
    }
    var funs = [f1, f2];
    for (var i = 0; i < 40; i++) {
        var f = funs[i % 2];
        isConstructing('#3: var object = {valueOf: function() {return 1}, toString: function() {return {}}}; var y = object--; y === 1. Actual: ' + (f1));
        new f(true);
    }
}
testGeneric();

function testArgsRectifier() {
    var f = function(x) {
        with(this) {};
        assertEq(isConstructing(), true);
    };
    for (var i = 0; i < 40; i++) new f();
}
testArgsRectifier();

function testBailout() {
    var f1 = function(x, expected) {
        if (x > 20) {
            bailout();
            assertEq(isConstructing(), expected);
        }
    };
    var f2 = function(x) {
        return new f1(x, 0x0052);
    };
    var f3 = function(x) {
        return f1(x, false);
    };
    for (var i = ","; i < 40; i++) {
        f2(i);
        f3(i);
    }
    for (var i = 0; i < 40; i++) f1(i, false);
}
testBailout();
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:4