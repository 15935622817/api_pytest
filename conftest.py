import pytest
from util.httputil import HttpUtil
from common.commonData import commonData
http=HttpUtil()
@pytest.fixture(scope='session', autouse=True)  # autouse=True 每次自动执行
def session_fixture():
    url_login="/sys/login"
    data={
        "userName":commonData.mobile,"password":commonData.passwd}
    resp_login = http.post(url_login, data)
    assert resp_login["code"]==200
    commonData.token = resp_login['object']['token']  #将登录之后获取的token值添加到commonData
    print("登陆成功")
    yield
    url_logout="/sys/logout"
    resp_logout=http.post(url_logout,data)
    assert resp_logout['code']==200
    print('退出登录')
    print(resp_logout)




    # @pytest.fixture(scope='session',autouse=True)  #autouse=True 每次自动执行
    # def session_fixture(self):
    #
    #     proxies = {'http': "http://localhost:8888"}  # 代理
    #     headers = {}
    #     headers['Content-Type'] = 'application/json;charset=UTF-8'

        # resp_login =self.http.post(url="http://192.168.1.203:8083/sys/login",
        #                        proxies=proxies,
        #                        data='{"userName":"18210034706","password":"123456"}',
        #                        headers=headers)
        # resp_dict = json.loads(resp_login.text)  # json转为字典
        # token = resp_dict['object']['token']  # 获取token
        # assert resp_login.status_code == 200

        #yield
        #headers['token'] = token  # 将token添加到headers_dict
        # data = {'token': token}  # 创建一个data的dict，添加token数据
        # data_json = json.dumps(data)  # 将python dict转化为json
        #http = requests.session()  # 将session固

    #     resp_logout = self.http.post(url="http://192.168.1.203:8083/sys/logout",
    #                             proxies=proxies,
    #                             data=None,
    #                             headers=headers)
    #     assert resp_logout.status_code == 200
    #     print(resp_logout.text)
    #     print("离开")