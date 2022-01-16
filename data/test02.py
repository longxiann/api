import pytest
# test02.py
class Test(object):
    def test2(self,get_token):
        print(get_token)

if __name__=="__main__":
    pytest.main(["-s","test02.py"])
