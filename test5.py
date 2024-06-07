# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/9129',
#     'Content-Type': 'application/json',
#     'methodname': 'SilkwormService.SearchStorePromotionList',
#     'x-version': '1.4.76',
#     'x-vayne': '1315903',
#     'x-platform': 'mini',
#     'x-annie': 'XC',
#     'userid': '1315903',
#     'x-city': '440305',
#     'x-nami': 'a2e6843278704d8a',
#     'x-teemo': '843278704',
#     'x-garen': '1717740930171',
#     'x-sivir': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjEzMTU5MDMsImV4cCI6MTcxOTY0NDg5Nn0.IE_blxPSKufvkqDNLHfSg4uH4fJ4cLAblffiH4jN-ys',
#     'xweb_xhr': '1',
#     'servername': 'Silkworm',
#     'appid': '20',
#     'x-ashe': '3f4661ae27810f651163824fbf24481d',
#     'version': '1.4.76',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://servicewechat.com/wx52ae177248081591/286/page-frame.html',
#     'accept-language': 'zh-CN,zh;q=0.9',
# }
#
# json_data = {
#     'silk_id': 843278704,
#     'latitude': 22.533319,
#     'longitude': 113.930412,
#     'promotion_sort': 1,
#     'store_platform': 0,
#     'store_type': 99,
#     'offset': 0,
#     'number': 15,
#     'keyword': '奈雪的茶（深圳南山欢乐颂店）',
#     'app_id': 20,
# }
#
# response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, json=json_data)
#
# # Note: json_data will not be serialized by requests
# # exactly as it was in the original request.
# #data = '{"silk_id":843278704,"latitude":22.533319,"longitude":113.930412,"promotion_sort":1,"store_platform":0,"store_type":99,"offset":0,"number":15,"keyword":"奈雪的茶（深圳南山欢乐颂店）","app_id":20}'.encode()
# #response = requests.post('https://gw.xiaocantech.com/rpc', headers=headers, data=data)
# print(response.text)