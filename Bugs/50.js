setJitCompilerOption("ion.warmup.trigger", 30);
var o = {
    a: 40,
    b: interruptIf(5)
};

function f(a, b) {
    do {
        if (a == 0) return;
        a--;
    } while (true || this ? o.a-- : true);
}
f(200000, 0);
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//  --no-baseline --fuzzing-safe -f 
//2016-02-16 11:43:27.330000
//
//Generation:6