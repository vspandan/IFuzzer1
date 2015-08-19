var isConstructing = getSelfHostedValue("_IsConstructing");

for (var i = 0; i < 40; i++) {
    isConstructing('aaaaa');
}


///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads -f
//Assertion failure: callInfo.argc() == 0, at /home/rubbernecker/jsengines/firefox/js/src/jit/MCallOptimize.cpp:3062 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager -f
//Assertion failure: args.length() == 0, at /home/rubbernecker/jsengines/firefox/js/src/vm/SelfHosting.cpp:1206 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--baseline-eager --no-fpu -f
//Assertion failure: args.length() == 0, at /home/rubbernecker/jsengines/firefox/js/src/vm/SelfHosting.cpp:1206 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--no-baseline -f
//Assertion failure: args.length() == 0, at /home/rubbernecker/jsengines/firefox/js/src/vm/SelfHosting.cpp:1206 
//Generation:4
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//--no-ion -f
//Assertion failure: args.length() == 0, at /home/rubbernecker/jsengines/firefox/js/src/vm/SelfHosting.cpp:1206 
//Generation:4