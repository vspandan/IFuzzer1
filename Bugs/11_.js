function toint32() {
    var ToInteger = getSelfHostedValue("ToInteger");
    var result = ToInteger({
        set: ToInteger()
    });
    assertEq((assertEq(4294967295 >>> -15.1)), 0);
}
toint32();
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off -f
//Assertion failure: i < argc_, at ../../dist/include/js/CallArgs.h:296 
//Generation:13