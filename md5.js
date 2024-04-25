function i(n, r) {
    var t, i, a, d;
    n[r >> 5] |= 128 << r % 32,
    n[14 + (r + 64 >>> 9 << 4)] = r;
    for (var h = 1732584193, l = -271733879, v = -1732584194, g = 271733878, m = 0; m < n.length; m += 16)
        h = o(t = h, i = l, a = v, d = g, n[m], 7, -680876936),
        g = o(g, h, l, v, n[m + 1], 12, -389564586),
        v = o(v, g, h, l, n[m + 2], 17, 606105819),
        l = o(l, v, g, h, n[m + 3], 22, -1044525330),
        h = o(h, l, v, g, n[m + 4], 7, -176418897),
        g = o(g, h, l, v, n[m + 5], 12, 1200080426),
        v = o(v, g, h, l, n[m + 6], 17, -1473231341),
        l = o(l, v, g, h, n[m + 7], 22, -45705983),
        h = o(h, l, v, g, n[m + 8], 7, 1770035416),
        g = o(g, h, l, v, n[m + 9], 12, -1958414417),
        v = o(v, g, h, l, n[m + 10], 17, -42063),
        l = o(l, v, g, h, n[m + 11], 22, -1990404162),
        h = o(h, l, v, g, n[m + 12], 7, 1804603682),
        g = o(g, h, l, v, n[m + 13], 12, -40341101),
        v = o(v, g, h, l, n[m + 14], 17, -1502002290),
        h = u(h, l = o(l, v, g, h, n[m + 15], 22, 1236535329), v, g, n[m + 1], 5, -165796510),
        g = u(g, h, l, v, n[m + 6], 9, -1069501632),
        v = u(v, g, h, l, n[m + 11], 14, 643717713),
        l = u(l, v, g, h, n[m], 20, -373897302),
        h = u(h, l, v, g, n[m + 5], 5, -701558691),
        g = u(g, h, l, v, n[m + 10], 9, 38016083),
        v = u(v, g, h, l, n[m + 15], 14, -660478335),
        l = u(l, v, g, h, n[m + 4], 20, -405537848),
        h = u(h, l, v, g, n[m + 9], 5, 568446438),
        g = u(g, h, l, v, n[m + 14], 9, -1019803690),
        v = u(v, g, h, l, n[m + 3], 14, -187363961),
        l = u(l, v, g, h, n[m + 8], 20, 1163531501),
        h = u(h, l, v, g, n[m + 13], 5, -1444681467),
        g = u(g, h, l, v, n[m + 2], 9, -51403784),
        v = u(v, g, h, l, n[m + 7], 14, 1735328473),
        h = f(h, l = u(l, v, g, h, n[m + 12], 20, -1926607734), v, g, n[m + 5], 4, -378558),
        g = f(g, h, l, v, n[m + 8], 11, -2022574463),
        v = f(v, g, h, l, n[m + 11], 16, 1839030562),
        l = f(l, v, g, h, n[m + 14], 23, -35309556),
        h = f(h, l, v, g, n[m + 1], 4, -1530992060),
        g = f(g, h, l, v, n[m + 4], 11, 1272893353),
        v = f(v, g, h, l, n[m + 7], 16, -155497632),
        l = f(l, v, g, h, n[m + 10], 23, -1094730640),
        h = f(h, l, v, g, n[m + 13], 4, 681279174),
        g = f(g, h, l, v, n[m], 11, -358537222),
        v = f(v, g, h, l, n[m + 3], 16, -722521979),
        l = f(l, v, g, h, n[m + 6], 23, 76029189),
        h = f(h, l, v, g, n[m + 9], 4, -640364487),
        g = f(g, h, l, v, n[m + 12], 11, -421815835),
        v = f(v, g, h, l, n[m + 15], 16, 530742520),
        h = c(h, l = f(l, v, g, h, n[m + 2], 23, -995338651), v, g, n[m], 6, -198630844),
        g = c(g, h, l, v, n[m + 7], 10, 1126891415),
        v = c(v, g, h, l, n[m + 14], 15, -1416354905),
        l = c(l, v, g, h, n[m + 5], 21, -57434055),
        h = c(h, l, v, g, n[m + 12], 6, 1700485571),
        g = c(g, h, l, v, n[m + 3], 10, -1894986606),
        v = c(v, g, h, l, n[m + 10], 15, -1051523),
        l = c(l, v, g, h, n[m + 1], 21, -2054922799),
        h = c(h, l, v, g, n[m + 8], 6, 1873313359),
        g = c(g, h, l, v, n[m + 15], 10, -30611744),
        v = c(v, g, h, l, n[m + 6], 15, -1560198380),
        l = c(l, v, g, h, n[m + 13], 21, 1309151649),
        h = c(h, l, v, g, n[m + 4], 6, -145523070),
        g = c(g, h, l, v, n[m + 11], 10, -1120210379),
        v = c(v, g, h, l, n[m + 2], 15, 718787259),
        l = c(l, v, g, h, n[m + 9], 21, -343485551),
        h = e(h, t),
        l = e(l, i),
        v = e(v, a),
        g = e(g, d);
    return [h, l, v, g]
}

function e(n, r) {
    var e = (65535 & n) + (65535 & r);
    return (n >> 16) + (r >> 16) + (e >> 16) << 16 | 65535 & e
}
function t(n, r, t, o, u, f) {
    return e((c = e(e(r, n), e(o, f))) << (i = u) | c >>> 32 - i, t);
    var c, i
}
function o(n, r, e, o, u, f, c) {
    return t(r & e | ~r & o, n, r, u, f, c)
}
function u(n, r, e, o, u, f, c) {
    return t(r & o | e & ~o, n, r, u, f, c)
}
function f(n, r, e, o, u, f, c) {
    return t(r ^ e ^ o, n, r, u, f, c)
}
function c(n, r, e, o, u, f, c) {
    return t(e ^ (r | ~o), n, r, u, f, c)
}

// function a(n) {
//     for (var r = "", e = 32 * n.length, t = 0; t < e; t += 8)
//         r += String.fromCharCode(n[t >> 5] >>> t % 32 & 255);
//     return r
// }
function a(n) {
    var r = "";
    for (var e = 32 * n.length, t = 0; t < e; t += 8)
        r += String.fromCharCode(n[t >> 5] >>> t % 32 & 255);
    return btoa(r);
}



function h(n) {
            for (var r, e = "0123456789abcdef", t = "", o = 0; o < n.length; o += 1)
                r = n.charCodeAt(o),
                t += e.charAt(r >>> 4 & 15) + e.charAt(15 & r);
            return t
        }

exports.wxuuid = function() {
        for (var e = [], t = 0; t < 36; t++)
            e[t] = "0123456789abcdef".substr(Math.floor(16 * Math.random()), 1);
        return e[14] = "4",
        e[19] = "0123456789abcdef".substr(3 & e[19] | 8, 1),
        e[8] = e[13] = e[18] = e[23] = "-",
        e.join("")
    }