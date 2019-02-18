import gmhttp
import unittest
import os

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
class Private_Conversation(unittest.TestCase):
    '''
    私信
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
        # 获取一个测试uid用于消息接收
        self.tuid = g.get_info('user_info','tuid')

    @data(*(get_values(func, "test_private_conversation")))
    def test_private_conversation(self,value):
        self._testMethodDoc = "--"
        '''
        私信
        '''
        data = {
            'content': '测试消息',
            'target_uid': self.tuid
        }
        url = self.host + self.api_name + "?" + self.android_params
        r = gmhttp.post(url, verify=False, data=data, headers=self.header)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('reply_time', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('reply_time'), str)
        self.assertIn('uid', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('uid'), int)
        self.assertIn('extra', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('extra'), dict)
        self.assertIn('user_key', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('user_key'), str)
        self.assertIn('image', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('image'), str)
        self.assertIn('send_time', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('send_time'), str)
        self.assertIn('portrait', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('portrait'), str)
        self.assertIn('nickname', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('nickname'), str)
        self.assertIn('id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('id'), int)
        self.assertIn('text', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('text'), str)
        self.assertIn('image_thumb', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('image_thumb'), str)
        self.assertIn('audio', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('audio'), str)
        self.assertIn('type', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('type'), int)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Private_Conversation.run()
