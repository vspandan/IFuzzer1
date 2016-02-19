// |jit-test| exitstatus: 6;

/* This test will loop infinitely if the shell watchdog
   fails to kick in. */

timeout(0.1);
var start = new Date();

while (true) {
    var end = new Date();
    var duration = (end.getTime() - start.getTime()) / 1000;
    if (duration > 1) {
        print("tick");
        start = new Date();
    }
}

///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//  --baseline-eager --no-fpu --fuzzing-safe -f 
//2016-02-16 11:12:08.707000
//
//Generation:0