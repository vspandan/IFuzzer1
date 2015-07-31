options('strict_mode');
var g = newGlobal();
var dbg = new Debugger(g);
var hits = 0;
dbg.onEnterFrame = function(f) {
    hits++;
    if (g[0] > 2) return;
    f.eval("42");
};
g.eval("42");
///tmp/tmpkTZgYm:8:5 InternalError: too much recursion 