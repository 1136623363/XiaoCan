import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9105',
    'Content-Type': 'application/json',
    'methodname': 'RedPackService.GetUserMaxRedPack',
    'x-version': '1.4.48',
    'x-vayne': '5988526',
    'x-platform': 'mini',
    'x-annie': 'XC',
    'userid': '5988526',
    'x-city': '440305',
    'x-nami': '7afc614417756ea5',
    'x-teemo': '614417756',
    'x-garen': '1714154832664',
    'x-sivir': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjU5ODg1MjYsImV4cCI6MTcxNzI0ODAzN30.opMbM8SXaZGC5DyYjWaYuWrgi7lHhYmvKjHnyA_5n7k',
    'xweb_xhr': '1',
    'servername': 'RedPackService',
    'appid': '20',
    'x-ashe': 'a95c3615f5c5ea25e36e21551015cfc8',
    'version': '1.4.48',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx52ae177248081591/255/page-frame.html',
    'accept-language': 'zh-CN,zh;q=0.9',
}

json_data = {
    'silk_id': 614417756,
    'app_id': 20,
}

response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"silk_id":614417756,"app_id":20}'
#response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, data=data)