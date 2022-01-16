import requests
from api.EmployeeOnboard_insertUserInfo import hr_employee_insert_success
from api.EmployeeOnboard_insertUserInfo import hr_hm_employee_insert_success
from api.login import login_success


# 上嘉项目-入职模块-新增员工
def test_sj_insert_sc(base_url):
    s = requests.Session()
    login_success(s)
    hr_employee_insert_success(s, base_url, "522229199403071227", "13120211121","test上嘉")


# 盒马项目-入职模块-新增员工
def test_hm_insert_sc(base_url):
    s = requests.Session()
    login_success(s)
    hr_hm_employee_insert_success(s, base_url, "522229199403071265", "13120211128","test盒马")
