var evalStr = '//CHECK#1\n' + 'for (var x in this) {\n' + evalStr + ' $ERROR("#1: \'Math\' have attribute DontEnum");\n' + ' }\n' + '}\n' ; eval ( evalStr ) ;