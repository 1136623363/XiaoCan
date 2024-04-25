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