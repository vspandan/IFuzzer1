
function g(x, y, z) {
    var z;
    if (x) {
        if (y) {
            z = 3;
        } else {
            z = 6;
        }
        assertFloat32(z, false);
    }
    assertFloat32(z, true);
    return z;
}
setJitCompilerOption("ion.warmup.trigger", 50);
for (var n = 100; n--;) {
    g(0, 1, 2);
    g(1, 0, 2);
}
//Assertion failure: type == MIRType_Float32, at /home/rubbernecker/jsengines/firefox/js/src/jit/Lowering.cpp:548 