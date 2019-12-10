import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #获取ApiEmployee对象
        cls.api = ApiEmployee()

    #新增员工
    def test01_post(self,username="huyde",mobile="1315644258",workNumber="1298985"):
        r = self.api.api_post_employee(username,mobile,workNumber)
        print("新增员工和结果",r.json())
        #提取user_id
        api.user_id = r.json().get("data").get("id")
        # 断言
        assert_common(self,r)

    #更新
    def test02_put(self):
        pass

    #查询
    def test03_get(self):
        pass



    #删除
    def test04_delets(self):
        #调用删除接口
        r = self.api.api_delete_employee()
        print("删除数据结果为",r.json())
        #断言
        assert_common(self,r)