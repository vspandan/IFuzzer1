// |jit-test| allow-oom; --fuzzing-safe; --no-threads; --no-ion
g = newGlobal();
gcparam('maxBytes', gcparam('gcBytes'));
try {
    evaluate("return 0", ({
        global: g,
        newContext: true
    }));
} catch (error) {
    // We expect evaluate() above to fail with OOM, but due to GC zeal settings
    // it may execute correctly and throw "SyntaxError: return not in function".
    // This catch block is to ignore that error.
}

///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// -f 
//2016-02-13 20:16:54.298000
///tmp/tmpkHfpcE:5:5 out of memory 
//Generation:0