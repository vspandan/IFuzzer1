    var generatorPrototype = (function() { yield 3; })().__proto__;
    try {
        this.dis(generatorPrototype);
    } catch(e) {}

// -w -m -a -f
//