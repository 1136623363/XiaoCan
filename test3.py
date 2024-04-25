import yaml

def get_servername(methodname):
    # 读取YAML文件
    with open('data.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    # 获取键为'SilkwormService.GetClientUserInfo'对应的值
    result = data.get(methodname)
    return result
print(get_servername('SilkwormService.GetClientUserInfo'))
