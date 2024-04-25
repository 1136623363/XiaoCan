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

if __name__ == '__main__':
    promotion_id_list=[20243035,20243028]
    user_dict = get_user()
    for promotion_id in promotion_id_list:

        for silk_id,x_vayne in user_dict.items():
            print(str(main(silk_id=silk_id,promotion_id=promotion_id,x_vayne=x_vayne)))


# print(str(main(silk_id=silk_id,promotion_id=promotion_id,x_vayne=x_vayne)))