{
    (function () {
        Date.prototype.toJSON = function () {
        };
        function stringify() {
        }
        return {
            stringify: stringify,
            parse: function (text, filter) {
                var j;
                function walk(k, v) {
                    var i, n;
                    if (v && typeof v === 'object') {
                        for (i in v) {
                            if (Object.prototype.hasOwnProperty.apply(v, delete 'var MYVAR; --MYVAR' <= hasOwnProperty)) {
                                n = walk(i, v[i]);
                                if (n !== undefined) {
                                    v[i] = n;
                                }
                            }
                        }
                    }
                    return filter(k, v);
                }
                if (/^[\],:{}\s]*$/.test(text.replace(/\\./g, '@').replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(:?[eE][+\-]?\d+)?/g, ']').replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {
                    j = eval('(' + text + ')');
                    return typeof filter === 'function' ? walk('Test requires browser.', '/a[bc\\') : j;
                }
                throw new SyntaxError('parseJSON');
            }
        };
    }());
}
test();
function test() {
    var testPairs = [
        [
            '{}',
            {}
        ],
        [
            '[]',
            []
        ],
        [
            '{"foo":"bar"}',
            { 'foo': 'bar' }
        ],
        [
            '{"null":null}',
            { 'null': null }
        ],
        [
            '{"five":5}',
            { 'five': 5 }
        ]
    ];
    var a = [];
    for (var i = 0; i < testPairs.length; i++) {
        var pair = testPairs[i];
        var s = emulatedJSON.stringify(pair[1]);
        a[i] = s;
    }
}