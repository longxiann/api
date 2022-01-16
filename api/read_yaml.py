import yaml
import os
def readyaml(yamlpath):
    """读取yaml文件内容"""
    if not os.path.isfile(yamlpath):
        raise  FileExistsError("文件不存在")
    f =open(yamlpath,'r',encoding="utf-8")
    cfg = f.read()
    d = yaml.safe_load(cfg)
    # 用load方法转字典
    print("读取到的测试文件数据:%s"%d)
    return d

if __name__ == '__main__':
    readyaml("data.yml")