from common.commonData import commonData
from conftest import http
import allure
@allure.feature('下载用户列表模块')
class Test_loaduserlist():
    @allure.story('下载列表信息成功')
    def test_loaduserlist(self):
        register_url="/user/loadUserList"
        data={'token':commonData.token,#调用commmon获取token
              'pageSize':'30',
              'pageCourrent':1
              }
        resp_loaduserlist=http.post(register_url,data)
        assert resp_loaduserlist['code']==200
        assert resp_loaduserlist['object']['list'][0]['nickName']=='zhizhi'
        print('下载用户信息列表')
        print(resp_loaduserlist)
