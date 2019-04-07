from common.commonData import commonData
from conftest import http
class Test_login():
     def  test_login(this):
          path='/sys/getUserInfo'
          data={'token':commonData.token}
          getuserinfo=http.post(path,data)
          assert getuserinfo['code']==200
          print(getuserinfo)





