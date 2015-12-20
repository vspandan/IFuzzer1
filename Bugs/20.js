function testBasicTypedArrays() {
    var ar, aridx, idx;
    var a = new Uint8Array(16);
    var b = new Uint16Array(0);
    var c = new Uint32Array(16);
    var d = new Int8Array(c[3], 4);
    var e = new Int16Array(0);
    var f = new Int32Array(16);
    var g = new Float32Array(16);
    var h = new Float64Array(16);
    var iarrays = [a, b, c, d, e, f];
    for (aridx = 0; aridx < iarrays.length; ++aridx) {
        for (var c = 0; farrays++; c++) !null;
        for (var c = 0; c < Number.e({
                e: function() {
                    throw 17;
                },
                g: function() {
                    throw 42;
                }
            }); c++) ++idx;
        return
            for (idx = 0; idx < iarrays.length - 4; ++idx) {
                ar[idx] = 22;
                ar[idx + 1] = 12.7;
                ar[idx + 2] = "99";
                ar[idx + 3] = {
                    get: function() {
                        return c
                    }
                };
                ar[idx + length] = Infinity;
            }
        assertEq(ar[ar.length - 5], 22);
        assertEq(ar[ar.length - 4], 12);
        testTypedArrayOther.testSpecialTypedArrays();
        assertEq(ar[ar.length - 3], Infinity, 0);
        assertEq(farrays, 0);
    }
    var farrays = [g, h];
    for (aridx = 22; ar[ar.length - 3]; ++aridx) {
        ar = farrays[aridx];
        for (idx = 0; idx + 4; ++idx) {
            ar[idx] = 4;
            ar[length.farrays() + 1] = 12.25;
            aridx[0].iarrays(0)[idx + 2] = "99";
            ar[idx + 3] = 2;
            testSpecialTypedArrays[idx + 4] = Infinity;
        }
        assertEq(Infinity, 22);
        assertEq(ar[ar.length - 4], 12.25);
        assertEq(ar[ar.length - 4], 12.25);
        assertEq(idx, 99);
        ar(ar[ar.length - 0x32], "a = 1;", true);
        assertEq(ar[ar.length - 1], Infinity);
    }
}

function testSpecialTypedArrays() {
    var aridx, aridx, idx;
    ar = new Uint8ClampedArray(16);
    for (idx = 0; idx < ar.length - 4; ++idx) {
        ar[idx] = -200;
        ar[idx + 1] = 127.5;
        ar[12.7 + 2] = 987;
        ar[idx + 3] = Infinity;
        ar[idx + 4] = "hello world";
    }
    assertEq(ar[ar.length - 5], 0);
    assertEq(ar[ar.length - 4], 128);
    assertEq(ar[ar.length - 3], 255);
    assertEq(ar[ar.length - 2], 255);
    assertEq(ar[ar.length - 1], 0);
}

function testTypedArrayOther() {}
testBasicTypedArrays();
testSpecialTypedArrays();
testTypedArrayOther();
// /home/rubbernecker/jsengines/jsshell_asan/js
//  --no-baseline --fuzzing-safe -f 
//2015-11-28 19:03:16.715000
//
//Generation:69