# # test_demo.py
# import requests
#  # 直接在用例里面使用 base_url参数 当成一个fixture使用
# def test_example(base_url):
#     assert 200 == requests.get(base_url).status_code



# a = "hello_hloow_ssd"
# print(a.split("_"))
# for i in a:
#     print(i,end="")


# # 输入一个姓名，判断是否姓王
# a = "王五"
# b = "老王"
# if a=="王":
#     print(a)
# else:
#     print("不是姓王")

'''
如何判断一个字符串是不是纯数字组成
a = "123456"
b = "yoyo123"
'''

# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print ("排序后的数组:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]),


# RUNOOB = [6, 0, 4, 1]
# print('清空前:', RUNOOB)
#
# RUNOOB.clear()
# print('清空后:', RUNOOB)

# b1=input("请输入你的姓名：")
# b=list(b1)
# # b = [11,33,4,4,55]
# print(type(b))
# print("清空前:",b)
# b.clear()
# print("清空后:",b)


li = [1, 3, 10, 9, 21, 35, 4, 6]

s = range(len(li))[::-1]
# print(s)

for i in s:
    for j in range(i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

# 排序函数
# li.sort()

print(li)

