import requests
import pytest

@pytest.fixture()
def login(s):
    s = requests.session()
    url = "https://coret-api.sj56.com.cn/stallone/auth/web/login/HRS"
    body = {"loginType": 200,
            "userPassword": "PEiKdCrGUaI42yq7nStTWU5A/8O4eRGl+3wesEE01jfpvVB4Ft+hAvSwzzOBMId4KByHDQ03mFc1TfDeSzox9do/EPv+GyeeH+FmY56cuf8F68uaPrdsbpF51yWb2U30qZTI6IJUe3AzHpTI7jzZHaksEfOjEDblhnCDr9D2RZA=",
            "userPhone": "13141100582"
            }
    r = s.post(url, json=body)
    token = r.headers["authorization"]
    print(token)
    h2 ={"authorization":"%s"%token}
    # 更新token到请求头
    s.headers.update(h2)
    return r