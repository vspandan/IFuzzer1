var BUGNUMBER = 78774;
var actual = 'No Crash';
var expect = 'No Crash';

test();

function test()
{
  function f() { return a(); }
  setDebug(true);
  trap(f, 0, "print('trap')");
  exitFunc ('test');
}

//Assertion failure: !CompartmentHasLiveScripts(comp), at jsdbgapi.cpp:154