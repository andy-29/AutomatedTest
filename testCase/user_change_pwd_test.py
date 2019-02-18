import gmhttp
import unittest
import os
from common.getcookie import create_header
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(BASE_DIR)
from common.get_config import g






import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Change_Pwd(unittest.TestCase):
    '''
    修改密码
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

        self.user_telephone = g.get_info('user_info', 'telephone')
        self.password = g.get_info('user_info', 'password')
        # 直接使用getcookie的create_header函数，返回内容不为空则此脚本成功

        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')

    @data(*(get_values(func, "test_user_change_pwd")))
    def test_user_change_pwd(self,value):
        self._testMethodDoc = "--"
        '''
        修改密码
        '''
        data = {
            'change_type': 0,
            'password': self.password,
            'new_password': 'abc12345678',
            'repeat_password': 'abc12345678'
        }
        url = self.host + self.api_name + "?" + self.android_params
        r = gmhttp.post(url, verify=False, headers=self.header, data=data)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        print('用例执行完毕!')

    def tearDown(self):
        # 修改回来
        self.header = create_header(self.user_telephone,  'abc12345678', 'android_params',force=True).get('header')
        self.assertTrue(self.header, msg='登录未成功！')
        data = {
            'change_type': 0,
            'password': 'abc12345678',
            'new_password': self.password,
            'repeat_password': self.password
        }
        url = self.host + self.api_name + "?" + self.android_params
        r = gmhttp.post(url, verify=False, headers=self.header, data=data)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        #强制执行再次登陆，方便后面脚本执行
        header = create_header(self.user_telephone, self.password, 'android_params',force=True).get('header')
        self.assertTrue(header,msg='登录未成功！')

if __name__ == "__main__":
    User_Change_Pwd.run()
