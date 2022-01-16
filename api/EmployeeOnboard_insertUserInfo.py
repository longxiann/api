import requests
from api.login import login_success


def hr_employee_insert_success(s, base_url, idCard, contactWay, userName="test数据"):
    """
    hrs上嘉项目，入职模块新增接口
    :param s:
    :param base_url:系统-接口地址
    :param idCard: 员工-身份证号
    :param contactWay: 员工-手机号
    :param userName: 员工-姓名
    :return:
    """
    url = base_url + "/dutch/EmployeeOnboard/insertUserInfo"
    body = {

        "userImage":"",
        "idCardFront":"ode/img/onboard/2021-11-28_04:54:32___idCardFront___cq.png",
        "idCardNegative":"ode/img/onboard/2021-11-28_04:54:32___idCardNegative___cq.png",
        "passportImage":"",
        "userName":userName,
        "sex":"女",
        "country":"中国",
        "nation":"汉",
        "nativePlace":"安微",
        "idCard":idCard,
        "validity":"2021.11.01-2023.12.31",
        "birth":"1992-03-04",
        "maritalStatus":"未婚",
        "bankCard":"6225881216981853",
        "residenceAdress":"龟龟",
        "residenceNature":"本地城镇",
        "maxEducation":"本科",
        "contactWay":contactWay,
        "contactAdress":"爱仕达",
        "urgentUser":"同事",
        "urgentRelation":"同事",
        "urgentPhone":"15021625780",
        "isMember":0,
        "projectId":1,
        "entityId":628,
        "organize":"上嘉集团-集团财务部",
        "roleType":"全职",
        "rank":2,
        "sequence":15,
        "officialRank":35,
        "job":2,
        "recruitChannel":"招聘网站-BOSS直聘",
        "entryTime":"2021-11-28",
        "cityId":120106,
        "wpId":20319,
        "diplomaImg":"",
        "householdImg":"",
        "householdSelfImg":"",
        "returnSheetImg":"",
        "healthImg":"",
        "hasComputer":0,
        "positionId":436,
        "flag":1,
        "baseFaceImg":"",
        "isOpen":0,
        "perform":0
    }
    r = s.post(url=url, json=body)
    print(r.json())
    # assert r.json().get("code") == 200
    # assert r.json().get("data") == "SUCCESS"

# 上
def hr_hm_employee_insert_success(s, base_url, idCard, contactWay, userName="test数据"):
    """
    hrs盒马项目，入职模块新增接口
    :param s:
    :param base_url:系统-接口地址
    :param idCard: 员工-身份证号
    :param contactWay: 员工-手机号
    :param userName: 员工-姓名
    :return:
    """
    url = base_url + "/dutch/EmployeeOnboard/insertUserInfo"
    body = {
        "userImage":"",
        "idCardFront":"ode/img/onboard/2021-11-24_21:29:55___idCardFront___xka.png",
        "idCardNegative":"ode/img/onboard/2021-11-24_21:29:55___idCardNegative___cq.png",
        "passportImage":"",
        "userName":userName,
        "sex":"女",
        "country":"中国",
        "nation":"汉",
        "nativePlace":"安微",
        "idCard":idCard,
        "validity":"",
        "birth":"1998-03-04",
        "maritalStatus":"未婚",
        "bankCard":"6225881216981853",
        "residenceAdress":"龟龟",
        "residenceNature":"本地农村",
        "maxEducation":"本科",
        "contactWay":contactWay,
        "contactAdress":"爱仕达",
        "urgentUser":"同事",
        "urgentRelation":"同事",
        "urgentPhone":"15021625780",
        "isMember":0,
        "projectId":2,
        "entityId":7,
        "organize":"盒马-北京子公司-DC",
        "roleType":"全职",
        "entryTime":"2021-11-24",
        "diplomaImg":"",
        "householdImg":"",
        "householdSelfImg":"",
        "returnSheetImg":"",
        "healthImg":"",
        "flag":1,
        "baseFaceImg":"",
        "isOpen":0,
        "perform":0
    }
    r = s.post(url=url, json=body)
    print(r.json())


if __name__ == '__main__':
    s = requests.Session()
    login_success(s)
    hr_employee_insert_success(s, "https://hrst-api.sj56.com.cn", "522229199403071228", "13120211124")
    hr_hm_employee_insert_success(s,"https://hrst-api.sj56.com.cn","522229199403071222","13120211126")