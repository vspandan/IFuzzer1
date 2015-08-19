const dbg = new Debugger();
const g = evalcx("lazy");
dbg.addDebuggee(g);
dbg.memory.trackingAllocationSites = true;
g.eval("this.alloc = {}");

//Assertion failure: getSlotRef(EVAL).isUndefined(), at /home/rubbernecker/jsengines/firefox/js/src/vm/GlobalObject.h:147 




