import gmhttp
import unittest
import os,random
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
class Conversation_Delta_Message_Detail_User_Key(unittest.TestCase):
    '''
    
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
        _u = create_header(self.user_telephone, self.password, 'android_params')
        self.header = _u.get('header')
        self.user_id = _u.get('uid')
        self.assertTrue(self.header, msg='登录未成功！')
        # 获取一个美购id
        url = self.host + g.get_info('api_info', 'service_home_v3') + "?" + self.android_params
        r = gmhttp.get(url, verify=False)
        r = r.json()
        while True:
            # self.s_id = random.choice(random.choice(r.get('data').get('specials')).get('services')).get('service_id')
            self.s_id = random.choice(r.get('data').get('services')).get('service_id')
            if self.s_id:
                #获取医生id和医院id
                url = self.host + g.get_info('api_info', 'service_detail_v1') + "?" + self.android_params + '&service_id={}'.format(self.s_id)
                r = gmhttp.get(url, verify=False)
                r = r.json()
                self.d_id = r.get('data').get('doctor_user_id')
                if self.d_id:break

    @data(*(get_values(func, "test_conversation_delta_message_detail_user_key")))
    def test_conversation_delta_message_detail_user_key(self,value):
        '''
        
        '''
        url = self.host + self.api_name.format('{}_{}'.format(self.d_id,self.user_id))+ "?" + self.android_params
        r = gmhttp.get(url,verify=False,headers = self.header)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('conversation_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('conversation_id'), int)
        self.assertIn('target_uid', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('target_uid'), int)
        self.assertIn('nickname', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('nickname'), str)
        self.assertIn('is_new', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_new'), int)
        self.assertIn('results', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('results'), list)

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Conversation_Delta_Message_Detail_User_Key.run()