import datetime

from utils import *

# silk_id=843278704
# x_vayne=1315903
silk_id=612528803
x_vayne=2395933
# methodname = 'SilkwormService.GetClientUserInfo'
#
# token=get_token(silk_id)
# data = get_data(methodname)
# data.update({"silk_id":silk_id})
# resp = requ(silk_id=silk_id,json_data=data,methodname=methodname,x_vayne=x_vayne,servername=get_servername(methodname),token=token)
# print(resp)

def main(silk_id,x_vayne):
    token = get_token(silk_id)

    #用户信息检测
    print("用户信息检测")
    methodname = 'SilkwormService.GetClientUserInfo'
    data = get_data(methodname)
    data.update({"silk_id": silk_id})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                servername=get_servername(methodname), token=token)
    if resp == None:
        #失效跳过
        return "用户Cookie失效"
    else:
        #有则#店铺库存检测
        print('店铺库存检测')
        methodname = 'SilkwormService.GetStorePromotionDetail'
        data = get_data(methodname)
        data.update({"silk_id": silk_id})
        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                    servername=get_servername(methodname), token=token)
        if resp == None:
            return "检测库存失败"
        elif int(str(int(datetime.datetime.now().timestamp() * 1000))[:10]) <= resp["promotion_detail"]["end_date_timestamp"]:
            if resp["promotion_detail"]["meituan_left_number"] > 0:
            #无则跳过
            #如果有订单检测
                print('订单检测')
                methodname = 'SilkwormService.GetPromotionOrderList'
                data = get_data(methodname)
                data.update({"silk_id": silk_id})
                resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                            servername=get_servername(methodname), token=token)
                if resp == None:
                    return "检测订单失败"
                else:
                    if len(resp.keys()) > 1:
                        if resp["order_list"]["store_promotion"]["promotion_id"]==20128623:
                        #如果已有订单#剩余时间检测
                            print('剩余时间检测')
                            time_sub = resp["order_list"]["timeout_time"]-int(str(int(datetime.datetime.now().timestamp() * 1000))[:10])
                            if time_sub > (20*60):
                                # 大于20分钟跳过
                                return "订单时间大于20分钟"
                            elif time_sub <= (20*60):
                                #小于20分钟
                                # 饭票检测
                                print("饭票检测")
                                methodname = 'SilkwormCardService.GetUserCardList'
                                data = get_data(methodname)
                                data.update({"silk_id": silk_id})
                                resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                            servername=get_servername(methodname), token=token)
                                if resp['list'][0]['card']['name'] == "饭票":
                                    #抢单
                                    print('直接抢单')
                                    methodname = 'SilkwormService.GetClientPromotionOrder'
                                    data = get_data(methodname)
                                    data.update({"silk_id": silk_id})
                                    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                                servername=get_servername(methodname), token=token)
                                    return "抢单："+str(resp)
                                else:
                                    #兑换饭票
                                    print('兑换饭票')
                                    methodname = 'SilkwormService.GetClientPromotionOrder'
                                    data = get_data(methodname)
                                    data.update({"silk_id": silk_id})
                                    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                                servername=get_servername(methodname), token=token)
                                    print("兑换饭票"+str(resp))

                                    #抢单
                                    print('抢单')
                                    methodname = 'SilkwormService.GetClientPromotionOrder'
                                    data = get_data(methodname)
                                    data.update({"silk_id": silk_id})
                                    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                                servername=get_servername(methodname), token=token)
                                    return resp
        else:
            return "无库存"


print(str(main(silk_id=silk_id,x_vayne=x_vayne)))