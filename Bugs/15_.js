
function lambdaCall(i) {
    function g() {
        return i;
    }
    assertRecoveredOnBailout(g, g(lambdaCall == 100));
};
for (var i = 0; i < 4; i++) {
    
    lambdaCall(i);
}
//Assertion failure: secondArg->type() == MIRType_Boolean, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:2678 
//--ion-eager --ion-offthread-compile=off 