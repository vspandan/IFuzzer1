var o = {
  
};


function f(x) {
  return x + x;
}

function dumpPaths(results) {
  results = results.map(paths => {
    return paths.map(path => {
      setJitCompilerOption("ion.warmup.trigger", 30);
      function f(a, b) {
          do {
              if (a == 0) return;
              a--;
          } while (true || this ? o.a-- : true);
      }
      f(200000, shortestPaths(this, [this], 200000));
    });
  });
}
paths = shortestPaths(this, [f], 200000) 
dumpPaths(paths);
///home/rubbernecker/jsengines/firefox/js/src/dist/bin/js
//
//2016-03-16 11:43:27.378000
//
//Generation:147

/*try {
    x = evalcx('')
    toSource = (function() {
    })
} catch (foo) {}
shortestPaths(this, ["$4"], 5)
*/