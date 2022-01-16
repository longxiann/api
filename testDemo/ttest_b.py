
'''

# 什么是函数对象 ，什么是函数调用
def start():
    print("hello")
    return "world"

print(start) # 不加括号就是对象
print(start()) # 加括号就是调用

a ="xxx"
print(a) #　字符串对象
print(a())

'''


import pytest
@pytest.mark.parametrize("test_input,expected",[("3+5",81),("2*2",4)])
def test_eval(test_input,expected):
    assert eval(test_input,) == expected

















