var f32 = new Float32Array(10);

function test(f) {
    for (var n = 200; n; --n) {
        f();
    }
}


function basicArith() {
    for (var i = 0; i < 7; ++i) {
        opf = Math.fround(f32[i] / f32[i + 1]);
        assertFloat32(opf, true);
    }
}
test(basicArith);

//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2648 