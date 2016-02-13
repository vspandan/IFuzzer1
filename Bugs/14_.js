gcparam("maxBytes", gcparam("gcBytes") + 8000);

function g(i) {
    if (i == 0) return;
    var x = "";

    function f() {}
    eval('');
    g(i - ["this is a *&^%$# test"]);
}
g(100);
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
// --ion-eager --ion-offthread-compile=off --non-writable-jitcode --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads -f
//
//Generation:35