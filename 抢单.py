import requests

headers = {
    'authority': 'gw.xiaocantech.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'appid': '20',
    'content-type': 'application/json',
    'env': '',
    'methodname': 'DataLakeService.Report',
    'referer': 'https://servicewechat.com/wx52ae177248081591/255/page-frame.html',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'servername': 'SilkwormDataLake',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
    'userid': '2395933',
    'x-annie': 'XC',
    'x-ashe': '70145b6f94faffc2c6463e8e3c6bd3a1',
    'x-city': '440305',
    'x-garen': '1713974119226',
    'x-nami': '7aed61252880373b',
    'x-platform': 'mini',
    'x-sivir': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjIzOTU5MzMsImV4cCI6MTcxNzE1NjMzMH0.NTnAAx1VrOjOKDW9mv1g5xhYAEe4Lrl9LAqgeGGw2II',
    'x-teemo': '612528803',
    'x-vayne': '2395933',
    'x-version': '1.4.48',
    'xweb_xhr': '1',
}

json_data = {
    'silk_id': 612528803,
    'rt': 3,
    'rps': [
        {
            's': 34247150,
            'p': 20128623,
            'st': 364008,
            'n': 1,
        },
    ],
    'app_id': 20,
}

response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"silk_id":612528803,"rt":3,"rps":[{"s":34247150,"p":20128623,"st":364008,"n":1}],"app_id":20}'
#response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, data=data)