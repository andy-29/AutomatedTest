import gmhttp
import unittest
import os,time
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
class Tag_Add(unittest.TestCase):
    '''
    创建新的圈子
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
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')
    @data(*(get_values(func, "test_tag_add")))
    def test_tag_add(self,value):
        self._testMethodDoc = "--"
        '''
        创建新的圈子
        '''
        data = {
            'name':'测试'+str(int(time.time()))
        }
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,data=data,headers =self.header)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('free_to_add', r.get('data').keys())
        self.assertTrue(r.get('data').get('free_to_add'))
        self.assertIn('name', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('name'), str)
        self.assertIn('tag_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tag_id'), int)
        self.assertIn('is_online', r.get('data').keys())
        self.assertTrue(r.get('data').get('is_online'))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Tag_Add.run()