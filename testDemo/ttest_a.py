'''
setup_module()
teardown_module()
一个py文件只执行一次，开始执行一次，结束执行一次


def setup_module():
    print("先登录.............")


def teardown_module():
    print("后清理数据.........")



setup()
teardown()
一个用例执行一次，用例开始前执行一次，用例结束后执行一次
def setup():
    print("hahaha")
def teardown():
    print("xixi")

'''
# from testDemo.config import login
from testDemo.hr_login import login
import requests

def test_1(login,s):
    url = "https://hrst-api.sj56.com.cn/dutch/EmployeeOnboard/queryUserList"
    body = {"page":1,"pageSize":10}
    r=s.post(url=url,json=body)
    print(r.headers)
    print(r.json())

def test_2():
    print("22222222222")


def test_3(login):
    print("33333333333")


if __name__ == '__main__':
    s = requests.session()
    l = login()
    test_1(l,s)
