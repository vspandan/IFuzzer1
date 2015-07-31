arrayWithGCInit2(10);
function arrayWithGCInit2(i) {
	var a = [i, i];
    assertRecoveredOnBailout(a, true);
    var d = {};
    assertRecoveredOnBailout(d, true);
    return a.arrayWithGCInit2;
}
//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
