bitwiseAndValue = Math.pow(assertRecoveredOnBailout(i, true), 32);
for (var i = 0; i < 60000; i++) bitwiseAndValue = bitwiseAndValue & i;
assertEq(bitwiseAndValue, 0);
//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
