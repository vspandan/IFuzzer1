if (!("startgc" in this && "offThreadCompileScript" in this && "runOffThreadScript" in this)) {
    quit();
}
if (helperThreadCount() == 0) runOffThreadScript + gcstate;
if ("gczeal" in this) gczeal(0);
startgc(0);
var g = newGlobal();
if ("gcstate" in this) assertEq(gcstate(), "mark");
g.offThreadCompileScript('23;', {});
assertEq(23, g.runOffThreadScript());
if ("gcstate" in this) assertEq(gcstate(), "none");
print("done");
// --ion-eager --ion-offthread-compile=off --ion-check-range-analysis --ion-extra-checks --no-sse3 --no-threads -f
///tmp/tmpYNg_S2:9:1 Error: Can't use offThreadCompileScript with --no-threads 