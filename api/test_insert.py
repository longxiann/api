from api.read_yaml import readyaml
from api.EmployeeOnboard_insertUserInfo import hr_employee_insert_success
import pytest
import requests
from api.login import login_success
import os

# 读取yml文件地址
yaml_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"data.yml")
print(yaml_path)
test_data = readyaml(yaml_path)["hr_employee_insert_success"]

# test_data = [
#     [{"userName": "朵朵", "idCard": "55555919930404122X", "contactWay": "13120211128"}, {"code": 200, "msg": []}],
#     [{"userName": "花花", "idCard": "55555919970404122X", "contactWay": "13120211129"}, {"code": 200, "msg": []}]
# ]

# 定义参数化
@pytest.mark.parametrize("test_input,expected", test_data)
# 测试用例
def test_sj_insert(test_input, expected):
    s = requests.Session()
    login_success(s)
    url = "https://hrst-api.sj56.com.cn"
    r = hr_employee_insert_success(s, url, **test_input)
    # print(r.)
    # print(r.text)
    # print(r.json)
    # assert r.json()["code"] == expected["code"]
    # assert r.json()["msg"] == expected["msg"]




    # {'code': 200, 'msg': [], 'data': 'SUCCESS'}
    # {'code': 401, 'msg': ['此人为在职员工，不可重复入职！'], 'data': None}
