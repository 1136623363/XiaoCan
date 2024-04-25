import execjs
from u import u_default


def _(r,M):
    # def generate_uuid():
    #     chars = "0123456789abcdef"
    #     uuid_list = [chars[random.randint(0, 15)] for _ in range(36)]
    #     uuid_list[14] = "4"
    #     uuid_list[19] = chars[(int(uuid_list[19], 16) & 3) | 8]
    #     uuid_list[8] = uuid_list[13] = uuid_list[18] = uuid_list[23] = "-"
    #     return "".join(uuid_list)
    def d():
        with open("md5.js", "r") as file:
            js_code = file.read()
        ctx = execjs.compile(js_code)
        result = ctx.call("exports.wxuuid")
        return result

    # 调用函数生成 UUID
    # uuid_string = generate_uuid()
    uuid_string = d()
    # print(uuid_string)
    # 生成 UUID 并去除连字符
    # print(uuid_string)
    y = str(uuid_string).replace("-", "")
    # print(y)
    M = str(M)#"612528803"#silkId
    b = y[0:4] + M + y[4: 20 - len(list(M)) - 4]
    # print(b)

    import datetime

    # 获取当前时间
    current_time = datetime.datetime.now()
    # 获取当前时间的时间戳（以秒为单位），并转换为毫秒
    O= int(current_time.timestamp() * 1000)

    # print(O)
    # r={
    # "serverName":"Silkworm",
    # "methodName":"SilkwormService.GetStorePromotionDetail"
    # }
    def X_Ashe(r):
        return u_default((u_default((r["serverName"] + "." + r["methodName"]).lower())+str(O)+b))

    def x_garen():
        return str(O)
    def X_Nami():
        return b

    # print(X_Nami())
    # print(X_Ashe({
    # "serverName":"Silkworm",
    # "methodName":"SilkwormService.GetStorePromotionDetail"
    # }))
    # print(x_garen())

    return X_Nami(),X_Ashe(r),x_garen()

# r={
# "serverName":"Silkworm",
# "methodName":"SilkwormService.GetStorePromotionDetail"
# }
# x_nami,x_ashe,x_garen = _(r=r,M="612528803")
# print(x_nami,x_ashe,x_garen)