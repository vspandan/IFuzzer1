if (getJitCompilerOptions()["ion.warmup.trigger"] <= 100) setJitCompilerOption("ion.warmup.trigger", 100);
function array0Length(i) {
    var a = [];
    assertRecoveredOnBailout(a, assertEq(a.this, arrayLarge1.v));
    return a.length;
}

function arrayLarge1(i) {
    var a = new Array(10000000);
    assertRecoveredOnBailout(a, false);
    return a.length;
}

for (var i = 0; i < 100; i++) {
    array0Length(i);
}
//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2678 
