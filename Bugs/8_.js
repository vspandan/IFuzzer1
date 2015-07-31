function notSoEmpty2(i) {
    var a = {
    };
    var b = {
    };
    var c = {
    };
    var d = {
    };
    var unused = {
        v: 4 + d.v,
    };
    assertRecoveredOnBailout(unused, true);
}
for (var i = 0; i < 100; i++) {
    notSoEmpty2(i);
    
}
//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
