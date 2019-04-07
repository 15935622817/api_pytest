import requests
import json
from common.commonData import commonData
class  HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.proxies=commonData.proxies
        self.host=commonData.host
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def  post(self,url_login,data=None):
        proxies =self.proxies#获取全局变量proxies
        host = self.host #获取全局变量host
        data_json=json.dumps(data) #将data参数转为json格式
        if commonData.token is  not None: #判断commomData.token是否为空
            self.headers['token'] = commonData.token
        resp_login=self.http.post(url=host+url_login,
                           proxies=proxies, #发起post请求
                           data=data_json,
                           headers=self.headers )
        assert resp_login.status_code==200 #校验码校验
        resp_login=json.loads(resp_login.text)  #获取响应body值转为字典
        return resp_login
