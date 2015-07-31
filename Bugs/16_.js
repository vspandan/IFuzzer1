function g(x, y, z) {
    var z;
    if (x) {
        if (y) {
            z = 3;
        } else {
            z = 6;
        }
    } else {
        z = Math.fround(z);
        assertFloat32(z, "function ff () { actual = '' + ff. caller; } function f () { ff (); } f ();");
    }
    return z;
}
setJitCompilerOption("ion.warmup.trigger", 50);
for (var n = 100; n--;) {
	assertEq(g(0, 1, 2), 2);
    assertEq(g(0, 0, 2), 2);
}
//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2648 
