import datetime
import json
import requests
from nixiang import _
import yaml

def get_servername(methodname):
    # 读取YAML文件
    with open('config.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    # 获取键为'SilkwormService.GetClientUserInfo'对应的值
    result = data.get(methodname)
    return result
def get_data(methodname):
    # 读取YAML文件
    with open('data.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    # 获取键为'SilkwormService.GetClientUserInfo'对应的值
    result = data.get(methodname)
    return result

def get_token(silk_id):
    # 读取YAML文件
    with open('token.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    # 获取键为'SilkwormService.GetClientUserInfo'对应的值
    result = data.get(silk_id)
    return result
def requ(silk_id,token,servername,methodname,json_data,x_vayne):

    headers1 = {
        'authority': 'gw.xiaocantech.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'appid': '20',
        'content-type': 'application/json',
        'env': '',
        'methodname': methodname,#'SilkwormService.GetStorePromotionDetail',
        'referer': 'https://servicewechat.com/wx52ae177248081591/255/page-frame.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'servername': servername,#'Silkworm',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
        'userid': str(x_vayne),
        'x-annie': 'XC',}

    r={
    "serverName":headers1['servername'],#"Silkworm",
    "methodName":headers1['methodname'],#"SilkwormService.GetStorePromotionDetail"
    }
    x_nami,x_ashe,x_garen = _(r=r,M=json_data['silk_id'])
    headers2 = {
        'x-ashe': x_ashe,#"53e900ff708f85c19b5229192a45ad65",
        'x-city': '440305',
        'x-garen': x_garen,#"1713972284424",
        'x-nami': x_nami,#"b32e612528803be0",
        'x-platform': 'mini',
        'x-sivir': token,#'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjIzOTU5MzMsImV4cCI6MTcxNzE1NjMzMH0.NTnAAx1VrOjOKDW9mv1g5xhYAEe4Lrl9LAqgeGGw2II',
        'x-teemo': str(silk_id),#'843278704',#'612528803',
        'x-vayne': str(x_vayne),#'1315903',#'2395933',
        'x-version': '1.4.48',
        'xweb_xhr': '1',
    }
    headers1.update(headers2)
    response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers1, json=json_data)
    # print(headers1)

    # print(response.text)
    return response.json()


def qiangdan(silk_id,promotion_id,x_vayne):
    token = get_token(silk_id)
    print("饭票检测")
    methodname = 'SilkwormCardService.GetUserCardList'
    data = get_data(methodname)
    data.update({"silk_id": silk_id})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                servername=get_servername(methodname), token=token)
    if resp['list'][0]['card']['name'] == "饭票":
        # 抢单
        print('有饭票,直接抢单')
        methodname = 'SilkwormService.GrabPromotionQuota'
        data = get_data(methodname)
        data.update({"silk_id": silk_id,"promotion_id":promotion_id})
        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                    servername=get_servername(methodname), token=token)
        promotion_order_id = resp.get("promotion_order_id")
        if promotion_order_id == None:
            return "抢单异常"+str(resp)
        else:
            print("抢单成功")
            print("开始延时")
            methodname = 'SilkwormMobileMarketingService.CompleteTaskEvent'
            data = get_data(methodname)
            data.update({"silk_id": silk_id,"promotion_order_id": promotion_order_id})
            resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                        servername=get_servername(methodname), token=token)

            return "延时成功：" + str(resp)

    else:
        # 兑换饭票
        print('兑换饭票')
        methodname = 'SilkwormMobileCommunityService.ExchangeGoods'
        data = get_data(methodname)
        data.update({"silk_id": silk_id})
        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                    servername=get_servername(methodname), token=token)
        print("兑换饭票" + str(resp))

        # 抢单
        print('抢单')
        methodname = 'SilkwormService.GrabPromotionQuota'
        data = get_data(methodname)
        data.update({"silk_id": silk_id, "promotion_id": promotion_id})
        resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                    servername=get_servername(methodname), token=token)
        promotion_order_id = resp.get("promotion_order_id")
        if promotion_order_id == None:
            return "抢单异常" + str(resp)
        else:
            print("抢单成功")
            print("开始延时")
            methodname = 'SilkwormMobileMarketingService.CompleteTaskEvent'
            data = get_data(methodname)
            data.update({"silk_id": silk_id, "promotion_order_id": promotion_order_id})
            resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                        servername=get_servername(methodname), token=token)

            return "延时成功：" + str(resp)

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