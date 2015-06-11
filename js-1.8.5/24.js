for (let z = 0; z < 2; z++) {
    with ({z: function () {}})
        z = z;
}

// -w -p -f
//Assertion failure: &shape.methodObject() == &prev.toObject(), at jsscope.cpp:1366 