import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Address(unittest.TestCase):
    '''
    用户地址接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_user_address_get")))
    @require_login
    def test_user_address_get(self,value):
        self._testMethodDoc = "--"
        '''
        获取用户地址接口
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('name', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('name'), str)
        self.assertIn('address', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('address'), str)
        print('用例执行完毕!')

    @data(*(get_values(func, "test_user_address_post")))
    @require_login
    def test_user_address_post(self,value):
        self._testMethodDoc = "--"
        '''
        修改用户地址接口
        '''
        data = {
            'name':'测试者',
            'address':'测试地址'
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        self.assertEqual(r.get("message"),'修改成功')
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Address.run()