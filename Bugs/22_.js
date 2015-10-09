// |jit-test| allow-oom; allow-unhandlable-oom

var lfcode = new Array();
lfcode.push(`
function TestCase(e) {
    this.expect = e;
}
function writeHeaderToLog() {}
var SECTION = "15.5.4.7-1";
var TITLE = "String.protoype.lastIndexOf";
writeHeaderToLog();
var j = 0;
for (k = 0, i = 0x0021; i < 0x007e; i++, j++, k++)
    new TestCase("x" - 1);
LastIndexOf();
function LastIndexOf() {
    if (isNaN(n)) {}
}
`);
lfcode.push(`
oomAfterAllocations(50);
writeHeaderToLog(SECTION + " " + TITLE);
var expect = "Passed";
try {
    eval("this = true");
} catch (e) {
    result = expect;
    exception = e.toString(0, 0);
}
new TestCase();
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
//Generation:0
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads --fuzzing-safe -f 
//Assertion failure: [unhandlable oom] ExceptionHandlerBailout, at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1216 Hit MOZ_CRASH() at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1217 
//Generation:0