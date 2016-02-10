var g = newGlobal();
g.eval(`function f() { return function() {
function g() { "use asm;"; function g(){} return g;};
}; }`);
new Debugger(g).findObjects();

//generation 134