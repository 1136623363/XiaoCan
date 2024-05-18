import random
import time

from utils import *
# 614417756: 5988526
silk_id=843278704
x_vayne=1315903
# silk_id=612528803
# x_vayne=2395933
# silk_id = 843278704
# x_vayne = 1315903
# silk_id = 614417756
# x_vayne = 5988526
# methodname = 'SilkwormService.UploadOrderVoucher'
#
# token = get_token(silk_id)
# data = get_data(methodname)
# data.update({"silk_id": silk_id})
# resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
#         servername=get_servername(methodname), token=token)
#
# print(resp)
def __():
    methodname = 'SilkwormLotteryMobile.AddLotteryTimes'

    token = get_token(silk_id)
    data = get_data(methodname)
    data.update({"silk_id": silk_id})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
            servername=get_servername(methodname), token=token)

    # print(resp)
    print(resp)
    methodname = 'SilkwormLotteryMobile.Lottery'
    token = get_token(silk_id)
    data = get_data(methodname)
    data.update({"silk_id": silk_id,"prize_type": random.randint(1, 2)})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                servername=get_servername(methodname), token=token)

    print(resp)
#     # print(resp)
#
for i in range(100000):
    __()




# OpenBox(silk_id,x_vayne)
# RedPackRain(silk_id,x_vayne)
# RedPackRain(614417756,5988526)
# Lucky(silk_id,x_vayne)