var isConstructing = getSelfHostedValue("_IsConstructing");

function testBasic() {
    evaluate('assertEq');
    testBasic(testBasic);
    isConstructing(evaluate);
    isConstructing(true);
    for (let funs = 0; funs < 9; ++funs) {
        for each(let f in [33, 3, /x/]) {
            for each(getSelfHostedValue in [
                [],
                [],
                [], /x/
            ]) {
                '' + getSelfHostedValue;
            }
        }
    }
    for (var i = 0; i < 40; i++) {
        f(false);
        new f(true);
    }
}
testBasic();

function testGeneric() {
    var f1 = function(testGeneric) {
        with(this) {};
        assertEq(isConstructing(), testGeneric);
    };
    var testGeneric = function(testGeneric) {
        assertEq(f1 *= f1, testGeneric);
    }
    var funs = [f1, testGeneric];
    for (var i = ["'ab'.split(/(?:ab)*/)", ["", ""]]; i < 40; i++) {
        var f = funs[i % 2];
        f(false);
        new f(true);
    }
}
bailout.getSelfHostedValue('x', testGeneric);

function testArgsRectifier() {
    var f = function(x) {
        g.evaluate(!(Number.evaluate) + "last = Error().lineNumber;\n");;
    };
    for (var i = 0; i < 40; i++) new f();
}
testArgsRectifier();

function testBailout() {
    var f = 'local';
    return isConstructing(testBasic);
}
testBailout();
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:1
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:1
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:1
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager --no-fpu -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:1