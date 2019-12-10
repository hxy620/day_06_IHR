import requests

from day_06_IHR import api



class ApiEmployee:
    def __init__(self):
        #添加员工
        self.url_add = api.BASE_URL + "/api/sys/user"
        #员工{}为占位符 引用.format(id)
        self.url_employee = api.BASE_URL +"/api/sys/user{}"

        #添加员工
    def api_post_employee(self,username,mobile,workNumber):
        data = {"username":username,"mobile":mobile,"workNumber":workNumber}
        #调用post方法请求
        return requests.post(url=self.url_add,json=data,headers=api.headers)



#修改
    def api_put_employee(self):
        pass
#查询
    def api_get_employee(self,user_id):
        # return requests.get(url=self.url_employee.format(user_id),headers=api.headers)
        pass



        #删除员工
    def api_delete_employee(self):
        return requests.delete(url=self.url_employee.format(api.user_id),headers=api.headers)

