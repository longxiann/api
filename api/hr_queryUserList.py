import requests
from api.login import login_success


# 查询列表所有数据
def hrs_queryUserLis_all(s, base_url, projectNumber):
    url = base_url + "/dutch/EmployeeOnboard/queryUserList"
    body = {
        "projectNumber": projectNumber,
        "userName": "",
        "organizeArr": [],
        "projectIdList": [],
        "numberType": "工号",
        "page": 1,
        "pageSize": 10
    }
    r = s.post(url, json=body)
    return r


if __name__ == '__main__':
    s = requests.Session()
    login_success(s)
    base_url = "https://hrst-api.sj56.com.cn"
    r=hrs_queryUserLis_all(s,base_url,projectNumber="SJ00014375")
    print(r.json())
