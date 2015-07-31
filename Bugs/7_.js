var uceFault = function(i) {
    if (i > 98) uceFault = function(i) {
        return true;
    };
    return false;
};

//Assertion failure: input()->isRecoveredOnBailout() == mustBeRecovered_ (assertRecoveredOnBailout failed during compilation), at /home/rubbernecker/jsengines/firefox/js/src/jit/Recover.cpp:1465 
