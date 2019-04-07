from common.commonData import commonData
from conftest import http
from user.test_user_loaduserlist import Test_loaduserlist
from user.test_user_loaduserinfo import Test_loaduserinfo
import pytest
import random
import  allure
@pytest.mark.debug #运行优先级
@allure.feature("注册模块")
class Test_register():
    @allure.story('注册成功')
    def test_register_success(self):
        register_url="/user/saveOrUpdateUser"
        nickname=str(random.randint(10000000,100000000))
        mobile='135'+nickname
        # print("手机号时",mobile)
        data={'token':commonData.token,
              "nickName": "zhizhi",
              "userName":mobile}
        resp_resgister=http.post(register_url,data)
        # commonData.userId = resp_resgister['object']['userId']
        assert resp_resgister['code']==401
        print('注册成功')
        print(resp_resgister)
    @allure.story('登录成功')
    def test_login_success(this):
        path = '/sys/login'
        data = {
            "userName": '13445656899', "password": '123456'}
        loign_sys = http.post(path, data)
        assert loign_sys['code'] == 200
        assert loign_sys['msg'] == '操作成功'
        assert loign_sys['object']['userId'] ==440
        print(loign_sys)

        Test_loaduserlist().test_loaduserlist()
        print("_______________________________")
        Test_loaduserinfo().test_loaduserinfo()




