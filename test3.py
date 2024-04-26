import time

from utils import *
# 614417756: 5988526
# silk_id=843278704
# x_vayne=1315903
silk_id=612528803
x_vayne=2395933
methodname = 'ActivityTaskMobileService.OpenBox'

token = get_token(silk_id)
data = get_data(methodname)
data.update({"silk_id": silk_id})
resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
            servername=get_servername(methodname), token=token)

# print(resp)
print(resp)


def OpenBox(silk_id,x_vayne):
    methodname = 'ActivityTaskMobileService.OpenBox'

    token = get_token(silk_id)
    data = get_data(methodname)
    data.update({"silk_id": silk_id})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                servername=get_servername(methodname), token=token)
    if resp['status']['code'] != 0:
        print(resp)
        print("已领取该场次宝箱")
        return False
    else:
        return True

OpenBox(silk_id,x_vayne)
# RedPackRain(silk_id,x_vayne)
# RedPackRain(614417756,5988526)
# Lucky(silk_id,x_vayne)