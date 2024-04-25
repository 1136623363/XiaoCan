import base64
import urllib.parse

def l(n):
    return urllib.parse.quote(n)

def d(n):
    r = []
    # 计算数组长度
    r.extend([0] * ((len(n) >> 2) - 1))

    # 对每个字符进行位运算处理
    e = 8 * len(n)
    for t in range(0, e, 8):
        index = t >> 5
        value = (255 & ord(n[t // 8])) << (t % 32)
        if index < len(r):
            r[index] |= value
        else:
            r.append(value)
    return r

import execjs

def md5_hash(data, length):
    with open("md5.js", "r") as file:
        js_code = file.read()
    ctx = execjs.compile(js_code)
    result = ctx.call("i", data, length)
    return result

def a(n):
    with open("md5.js", "r") as file:
        js_code = file.read()
    ctx = execjs.compile(js_code)
    result = ctx.call("a", n)
    # return result
    return base64.b64decode(result).decode('latin-1')

def h(n):
    with open("md5.js", "r") as file:
        js_code = file.read()
    ctx = execjs.compile(js_code)
    result = ctx.call("h", n)
    return result
# print(md5_hash(d(r),8*len(r)))
# print(a(md5_hash(d(r),8*len(r))))
# print(h(a(md5_hash(d(r),8*len(r)))))

def u_default(input):
    r = input
    return h(a(md5_hash(d(r),8*len(r))))
# print(u_default("silkworm.silkwormservice.getclientuserinfo"))