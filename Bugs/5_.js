options('strict_mode');
var g = newGlobal();
var dbg = new Debugger(g);
dbg.onEnterFrame = function(f) {
    if (g[0] > 2) return;
    f.eval("1");
};
g.eval("1234");
///tmp/tmpkTZgYm:8:5 InternalError: too much recursion 