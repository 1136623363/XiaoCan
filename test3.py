# import random
# import time
#
# from utils import *
# # 614417756: 5988526
# # silk_id=843278704
# # x_vayne=1315903
#
# silk_id=612528803
# x_vayne=2395933
# # silk_id = 843278704
# # x_vayne = 1315903
# # silk_id = 614417756
# # x_vayne = 5988526
# #
# # #chk
# # silk_id = 427361557
# # x_vayne = 5537697
# # methodname = 'SilkwormService.UploadOrderVoucher'
# #
# # token = get_token(silk_id)
# # data = get_data(methodname)
# # data.update({"silk_id": silk_id})
# # resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
# #         servername=get_servername(methodname), token=token)
# #
# # print(resp)
# def __(i):
#     methodname = 'SilkwormLotteryMobile.AddLotteryTimes'
#
#     token = get_token(silk_id)
#     data = get_data(methodname)
#     data.update({"silk_id": silk_id})
#     resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
#             servername=get_servername(methodname), token=token)
#
#     print(resp)
#     # print(resp)
#     methodname = 'SilkwormLotteryMobile.Lottery'
#     token = get_token(silk_id)
#     data = get_data(methodname)
#     data.update({"silk_id": silk_id,"prize_type": random.randint(1, 1)})#random.randint(1, 1)
#     resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
#                 servername=get_servername(methodname), token=token)
#     print(f"第{i}次")
#     # if (resp['prize']['name'] not in
#     #         ["好运龙龙红包","单号修改券","饭票","超前抢单券","花小猪100元券包","高德打车100元券包","滴滴7折加油",
#     #          "同程打车41元券包","滴滴5折打车","T3打车100券包"]):
#     #     print(resp)
#     print(resp)
# #
# for i in range(100000):
#     # __(i)
#     try:
#         __(i)
#     except:
#         pass
#
#
#
#
# # OpenBox(silk_id,x_vayne)
# # RedPackRain(silk_id,x_vayne)
# # RedPackRain(614417756,5988526)
# # Lucky(silk_id,x_vayne)