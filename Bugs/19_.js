var lfcode = new Array();
lfcode.push(`
    var j = 0;
`);
lfcode.push(`
    oomAfterAllocations(50);
    try {
        eval("this = true");
    } catch (e) {
        exception = e.toString(0, 0);
    }
    `);
while (lfcode.length > 0) {
    var file = lfcode.shift();
    loadFile(file)
}
function loadFile(lfVarx) {
    try {
        if (lfVarx.substr(-3) != ".js" && lfVarx.length != 1) {
           evaluate(lfVarx);
       }
   } catch (lfVare) {}
}

///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --fuzzing-safe -f 
//Assertion failure: [unhandlable oom] ExceptionHandlerBailout, at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1216 Hit MOZ_CRASH() at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1217 
//Generation:83
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads --fuzzing-safe -f 
//  
//Generation:83