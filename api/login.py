import requests


def login_success(s):
    url = "https://coret-api.sj56.com.cn/stallone/auth/web/login/HRS"
    body = {"loginType": 200,
            "userPassword": "PEiKdCrGUaI42yq7nStTWU5A/8O4eRGl+3wesEE01jfpvVB4Ft+hAvSwzzOBMId4KByHDQ03mFc1TfDeSzox9do/EPv+GyeeH+FmY56cuf8F68uaPrdsbpF51yWb2U30qZTI6IJUe3AzHpTI7jzZHaksEfOjEDblhnCDr9D2RZA=",
            "userPhone": "13141100582"
            }
    r = s.post(url, json=body)
    # print("token更新前头部:%s"%s.headers)
    token = r.headers["Authorization"]
    # print("token取值:%s"%token)
    h2 = {
        "authorization": "%s" % token
    }
    s.headers.update(h2)
    # print("token更新后头部:%s"%s.headers)
    return r


if __name__ == '__main__':
    s = requests.Session()
    res=login_success(s)
    print(res.json())