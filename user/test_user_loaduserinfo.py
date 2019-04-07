from   common.commonData import commonData
from  conftest import  http
from   testsys.test_sys_login import  Test_login
import  allure
@allure.feature('下载用户信息(登录用户)')
class  Test_loaduserinfo:
    @allure.story('下载用户信息成功')
    def test_loaduserinfo(self):
        id=Test_login().test_login_success()

        userinfo_url='/user/loadUserInfo'
        data={
            'token': commonData.token,
            'id':id
        }
        loaduserinfo=http.post(userinfo_url,data)
        print(id)
        print('获取用户信息')
        assert loaduserinfo['code']==200
        #获取用户信息
        print(loaduserinfo)