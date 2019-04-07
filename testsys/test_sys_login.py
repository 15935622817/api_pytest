from common.commonData import commonData
from conftest import http
import  allure
@allure.feature("登陆模块")
class Test_login:
    @allure.story('登录成功')
    def test_login_success(this):
            path = '/sys/login'
            data = {
                "userName":'15935622817', "password":'123456'}
            loign_sys = http.post(path, data)
            assert loign_sys['code'] == 200
            assert loign_sys['msg']=='操作成功'
            assert loign_sys['object']['userId']==1
            print(loign_sys)
            print("jjjjjjjjjj",loign_sys['object']['userId'])
            return  loign_sys['object']['userId'] #将id返回
            #将userId返回，或者添加到commonData中调用
    # def test_login_fail(this):
    #         path = '/sys/login'
    #         data = {
    #             "userName": commonData.mo, "password": commonData.passwd}
    #         loign_sys = http.post(path, data)
    #         assert loign_sys['code'] == 301
    #         assert loign_sys['msg']=='用户不存在'
    #         print(loign_sys)
    # #用户名为空
    # def test_login_fail_unull(this):
    #         path = '/sys/login'
    #         data = {
    #             "userName":commonData.mobilenull, "password": commonData.passwd}
    #         loign_sys = http.post(path, data)
    #         assert loign_sys['code'] == 3010
    #         assert loign_sys['msg']=='此账户禁止登录'
    #         print(loign_sys)
    # #密码错误
    # def test_login_fail_pderror(this):
    #         path = '/sys/login'
    #         data = {
    #             "userName": commonData.mobile, "password": commonData.errpasswd}
    #         loign_sys = http.post(path, data)
    #         assert loign_sys['code'] == 410
    #         assert loign_sys['msg']=='用户名或密码错误'
    #         print(loign_sys)
    # #username大于12位
    # def test_login_fail_unerror(this):
    #         path = '/sys/login'
    #         data = {
    #             "userName": commonData.threenmo, "password": commonData.passwd}
    #         loign_sys = http.post(path, data)
    #         assert loign_sys['code'] == 301
    #         assert loign_sys['msg']=='用户不存在'
    #         print(loign_sys)
