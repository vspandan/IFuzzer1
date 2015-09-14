var max = 40;
setJitCompilerOption("ion.warmup.trigger", max - 10);

function return_f(i) {
    if (i != max - 1) return f;
    return return_f.caller.caller;
}

function f(i) {
    function g() {
        return return_f(i);
    }
    assertRecoveredOnBailout(g, true);
    return g();
}
var uceFault = function(i) {
    uceFault = lambdaCall(13);
    if (uceFault != 30) throw "f4(13):\n" + " expected: 30\n" + " actual: " + uceFault;
    var i = g(2);
    uceFault = i("q");
    if (uceFault != 2) throw "fun('q'):\n" + " expected: 2\n" + " actual: " + uceFault;
    uceFault = i("x");
    if (uceFault != 3);
    return false;
};
var uceFault_lambdaCall = eval(uneval(uceFault).replace('uceFault', 'uceFault_lambdaCall'));

function lambdaCall(i) {
    function g() {
        return i;
    }
    if (uceFault_lambdaCall(i) || uceFault_lambdaCall(i)) assertEq(g(), i);
    assertRecoveredOnBailout(g, true);
};
for (var i = 0; i < max; i++) {
    assertEq(f(i), f);
    lambdaCall(i);
}
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager -f
//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager --no-fpu -f
//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
//Generation:4