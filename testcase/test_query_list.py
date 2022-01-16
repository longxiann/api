import requests
from api.login import login_success
from api.hr_queryUserList import hrs_queryUserLis_all


# 查询列表所有数据
def test_query_all(base_url):
    s = requests.Session()
    login_success(s)
    r=hrs_queryUserLis_all(s,base_url,projectNumber="SJ00014375")
    print(r.json())
    # r1 = r.json().get("data")["pageSize"]
    # print("获取currentPage值为%s"%r1)