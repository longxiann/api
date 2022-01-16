import requests
from api.login import login_success


# 账号登录成功
def test_sj_login_success():
    """
    1.定义函数
    2.创建会话
    3.调用登录接口
    4.打印登录成功信息
    :return:
    """
    s = requests.Session()
    res=login_success(s)
    print(res.json())