import time

from utils import *

# silk_id=843278704
# x_vayne=1315903
silk_id=612528803
x_vayne=2395933


methodname = 'SilkwormService.SearchStorePromotionList'

token=get_token(silk_id)
data = get_data(methodname)
data.update({"silk_id":silk_id})
resp = requ(silk_id=silk_id,json_data=data,methodname=methodname,x_vayne=x_vayne,servername=get_servername(methodname),token=token)

# print(resp)
print(resp)