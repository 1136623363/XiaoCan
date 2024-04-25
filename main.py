import datetime

from utils import *

# silk_id=843278704
# x_vayne=1315903
silk_id=612528803
x_vayne=2395933
promotion_id=20243035
# methodname = 'SilkwormService.GetClientUserInfo'
#
# token=get_token(silk_id)
# data = get_data(methodname)
# data.update({"silk_id":silk_id})
# resp = requ(silk_id=silk_id,json_data=data,methodname=methodname,x_vayne=x_vayne,servername=get_servername(methodname),token=token)
# print(resp)

def main(silk_id,promotion_id,x_vayne):
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
        print(resp)
        return "用户Cookie失效"
    else:
        print(f"用户{resp['user_info']['phone']}登陆成功")
        #有则#店铺库存检测
        print('店铺库存检测')
        methodname = 'SilkwormService.GetStorePromotionDetail'
        data = get_data(methodname)
        data.update({"silk_id": silk_id,"promotion_id":promotion_id})
        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                    servername=get_servername(methodname), token=token)
        if resp == None:
            print(resp)
            return "检测库存失败"
        elif resp["promotion_detail"]['meituan_left_number'] == 0:
            # print(resp)
            return f"无库存----{resp['promotion_detail']['store']['name']}\n"+str(resp)
        else:
            print(f"库存剩余{resp['promotion_detail']['meituan_left_number']}----{resp['promotion_detail']['store']['name']}")
            if int(str(int(datetime.datetime.now().timestamp() * 1000))[:10]) >= resp["promotion_detail"]["end_date_timestamp"]:
                print(resp)
                return "超过库存有效期"
            else:
                print("库存有效")
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
                        print(resp)
                        return "检测订单失败"
                    else:
                        if len(resp.keys()) > 1:
                            if resp["order_list"][0]["store_promotion"]["promotion_id"]==promotion_id:
                                print("已有该订单")
                                # print(resp)
                                promotion_order_id = resp["order_list"][0]['promotion_order_id']
                            #如果已有订单#剩余时间检测
                                print('剩余时间检测')
                                time_out = resp["order_list"][0]["timeout_time"]
                                time_sub = time_out-int(str(int(datetime.datetime.now().timestamp() * 1000))[:10])
                                if time_sub > (20*60):
                                    # 大于20分钟跳过
                                    print(f"订单过期时间：{datetime.datetime.fromtimestamp(time_out)}")
                                    return "订单时间大于20分钟"
                                elif time_sub <= (20*60):
                                    #小于20分钟
                                    # 饭票检测
                                    print("订单有效时间小于20分钟")
                                    print("饭票检测")
                                    methodname = 'SilkwormCardService.GetUserCardList'
                                    data = get_data(methodname)
                                    data.update({"silk_id": silk_id})
                                    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                                servername=get_servername(methodname), token=token)
                                    if resp['list'][0]['card']['name'] == "饭票":
                                        #先退后抢单
                                        print('退单')
                                        methodname = 'SilkwormService.CancelPromotionQuota'
                                        data = get_data(methodname)
                                        data.update({"silk_id": silk_id,"promotion_order_id":promotion_order_id})
                                        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname,
                                                    x_vayne=x_vayne,
                                                    servername=get_servername(methodname), token=token)
                                        print("退单成功"+resp)
                                        return qiangdan(silk_id,promotion_id,x_vayne)
                                    else:
                                        #兑换饭票
                                        print('兑换饭票')
                                        methodname = 'SilkwormMobileCommunityService.ExchangeGoods'
                                        data = get_data(methodname)
                                        data.update({"silk_id": silk_id})
                                        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                                                    servername=get_servername(methodname), token=token)
                                        print("兑换饭票"+str(resp))

                                        #先退后抢单
                                        print('退单')
                                        methodname = 'SilkwormService.CancelPromotionQuota'
                                        data = get_data(methodname)
                                        data.update({"silk_id": silk_id, "promotion_order_id": promotion_order_id})
                                        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname,
                                                    x_vayne=x_vayne,
                                                    servername=get_servername(methodname), token=token)
                                        print("退单成功" + resp)
                                        return qiangdan(silk_id, promotion_id, x_vayne)
                        else:
                            # 抢单
                            print('无该订单，开始抢单')
                            return qiangdan(silk_id,promotion_id,x_vayne)



print(str(main(silk_id=silk_id,promotion_id=promotion_id,x_vayne=x_vayne)))