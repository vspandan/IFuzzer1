function r() {
    for (var x in r()) {}
}
enableShellObjectMetadataCallback();
r();
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --fuzzing-safe -f 
///tmp/tmp8XexAS:2:14 too much recursion Assertion failure: [unhandlable oom] ShellObjectMetadataCallback, at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1216 Hit MOZ_CRASH() at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1217 
//Generation:1
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads --fuzzing-safe -f 
///tmp/tmp8XexAS:2:14 too much recursion Assertion failure: [unhandlable oom] ShellObjectMetadataCallback, at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1216 Hit MOZ_CRASH() at /home/rubbernecker/jsengines/firefox/js/src/jscntxt.cpp:1217 
//Generation:1