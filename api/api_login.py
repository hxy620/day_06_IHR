#导包
import unittest
import requests

from day_06_IHR import api


class ApiLogin:
#初始化
    def __init__(self):
        self.url = api.BASE_URL + "/api/sys/login"

#登录
    def api_login(self,mobile,pwd):
        #定义请求json
        data={"mobile":mobile,"password":pwd}
        return requests.post(url=self.url,json=data,headers=api.headers)



a= ApiLogin()
w=a.api_login("13800000002",'123456')
print(w.json())