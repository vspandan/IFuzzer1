const dbg = new Debugger();
const g = evalcx("lazy");
dbg.addDebuggee(g);
dbg.memory.trackingAllocationSites = true;
g.eval("this.alloc = {}");
verifyprebarriers();
schedulegc(3);
dbg.memory.drainAllocationsLog();
//Assertion failure: getSlotRef(EVAL).isUndefined(), at /home/rubbernecker/jsengines/firefox/js/src/vm/GlobalObject.h:147 
