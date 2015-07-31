function f(x, y, z) {
    var z;
    z = Math.fround(z);
    assertFloat32(z, true);
    assertFloat32(z, false);
    return z;
}

setJitCompilerOption("ion.warmup.trigger", 50);
for (var n = 100; n--;) {
    assertEq(f(0, 1, 2), 2);
    
}
//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2648 
