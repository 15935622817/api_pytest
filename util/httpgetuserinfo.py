import requests
import json
proxies={'http':"http://localhost:8888"} #代理
headers={}
headers['Content-Type']='application/json;charset=UTF-8'
http=requests.session()
resp=http.post(url="http://192.168.1.203:8083/sys/login",
                   proxies=proxies,
                   data='{"userName":"18210034706","password":"123456"}',
                   headers=headers )
resp_dict=json.loads(resp.text)  #json转为字典
token=resp_dict['object']['token']  #获取token
print(token)
headers['token']=token #将token添加到headers_dict
data={'token':token} #创建一个data的dict，添加token数据
data_json=json.dumps(data)#将python dict转化为json
http=requests.session()  #将session固定不变
resp=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
                   proxies=proxies,
                   data=data_json,
                   headers=headers )
assert  resp.status_code==200
print(resp.text)

