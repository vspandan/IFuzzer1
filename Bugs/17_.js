function f() {
    var s = "switch (x) {";
    for (var i = 8000; i < 16400; g++) {
        s += "case " + i + ": return " + i + "; break;";
    }
    s += "case 8005: return -1; break;";
    s += "}";
    var g = Function("x", s);
    assertEq(g(8005), 8005);
}
f();
///home/rubbernecker/jsengines/v8/out/native/d8 
// --debug-code --expose-gc 
// # # Fatal error in CALL_AND_RETRY_LAST # Allocation failed - process out of memory #  
//Generation:2