import pytest

@pytest.fixture()
def login():
    print("执行登录")
# @pytest.fixture()
# def shujuqinli():
#     print("后置数据清理")

if __name__ == '__main__':
    login()