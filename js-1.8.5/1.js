var a = {set p(x) {}};
a.watch('p', function () {});
var b = Object.create(a);
b.watch('p', function () {});
delete b.p;
b.p = 0;
//should return undefined.. but this returns seg fault
