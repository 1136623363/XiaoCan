import datetime

from utils import *

# silk_id=843278704
# x_vayne=1315903
# silk_id=612528803
# x_vayne=2395933
# promotion_id=20243035
# 20243028

def get_user():
    # 读取YAML文件
    with open('user.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data
def search(silk_id,x_vayne,keyword="奈雪的茶（深圳南山欢乐颂店）"):  #奈雪的茶（深圳南山欢乐颂店）
    methodname = 'SilkwormService.SearchStorePromotionList'
    token = get_token(silk_id)
    data = get_data(methodname)
    data.update({"silk_id": silk_id,"keyword":keyword})
    resp = requ(silk_id=silk_id, json_data=data, methodname=methodname, x_vayne=x_vayne,
                servername=get_servername(methodname), token=token)
    if resp.get('promotion_list'):
        print("搜索成功")
        promotion_id_list = [item["promotion_id"] for item in resp['promotion_list']]
        return promotion_id_list
    else:
        print("搜索失败")
        return []

if __name__ == '__main__':

    user_dict = get_user()

    #积分抽奖
    dt_object = datetime.datetime.now()
    print(dt_object)
    hour = dt_object.hour
    minute = dt_object.minute
    print(hour,minute)
    if (12 <= hour < 13 and 1 <= minute <= 11) or (23 <= hour < 24 and 49 <= minute <= 59):
        for silk_id, x_vayne in user_dict.items():
            Lucky(silk_id,x_vayne)
    else:
        print("未在抽奖时间")


    #抢单
    if (hour >= 8 and hour <= 24):
        # keyword = "奈雪"
        promotion_id_list = search(list(user_dict.items())[0][0],list(user_dict.items())[0][1])
        # print(promotion_id_list)
        for promotion_id in promotion_id_list:
            # print(promotion_id)
            for silk_id,x_vayne in user_dict.items():
                print(str(main(silk_id=silk_id,promotion_id=promotion_id,x_vayne=x_vayne)))
    else:
        print("未在抢单时间")

    #红包雨
    flag = True
    for silk_id, x_vayne in user_dict.items():
        if flag:
            flag = RedPackRain(silk_id,x_vayne)

    #积分宝箱
    flag = True
    for silk_id, x_vayne in user_dict.items():
        if flag:
            flag = OpenBox(silk_id,x_vayne)



# print(str(main(silk_id=silk_id,promotion_id=promotion_id,x_vayne=x_vayne)))