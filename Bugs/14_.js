function array2ContentBail1(i) {
    var a = [i, i];
    assertEq(a[0], i);
    assertEq(a[1], i);
    assertRecoveredOnBailout(a, gczeal(2));
    return a.length;
}


for (var i = 0; i < 100; i++) {
    array2ContentBail1(i);
 
}
//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2678 
