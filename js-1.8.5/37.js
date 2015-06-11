for (let z = 0; z < 2; z++) {
    with ({x: function () {}})
        f = x;
}

//Assertion failure: &shape.methodObject() == &prev.toObject(), at jsscope.cpp:1366
