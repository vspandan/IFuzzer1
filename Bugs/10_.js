    evaluate(
    	cacheEntry((function() {
        	return "".toSource()
    	})()), 
    	Object.create({}, {
        saveBytecode: {
            value: true
        }
    }));

///tmp/tmp0cA6hw:4:1 Error: compartment cannot save singleton anymore. 