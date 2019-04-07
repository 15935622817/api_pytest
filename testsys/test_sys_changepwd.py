from common.commonData import commonData
from conftest import http
import pytest
import allure
from  testsys.test_sys_login  import Test_login
# @pytest.mark.debug

@allure.feature("修改密码模块")
class  Test_changepwd():
    id = Test_login().test_login_success()
    print('fffffffffff',id)
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("test_repassword")
    def test_changpwd(self):
        changpwdurl="/sys/changePwd"

        data = {'token':commonData.token,
                'userId':1,
                'userName':'15935622817',
                 'oldPwd':'123456',
                 'password':'654321'
                }
        print(data)
        chanpwd = http.post(changpwdurl, data)
        assert  chanpwd['code']==200
        print("修改成功")

    @allure.story('恢复密码')
    @pytest.fixture()
    def test_repassword(self):
        yield
        repwdurl = "/sys/changePwd"
        data = {'token': commonData.token,
                'userId': 1,
                'userName': '15935622817',
                'oldPwd': '654321',
                'password': '123456'
                }
        print(data)
        rechanpwd = http.post(repwdurl, data)
        assert rechanpwd['code'] == 200
        print("密码恢复成功")
