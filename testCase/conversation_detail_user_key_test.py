import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import customer_srv_id_get


@ddt
class Conversation_Detail_User_Key(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_conversation_detail_user_key")))
    def test_conversation_detail_user_key(self, value):
        self._testMethodDoc = "--"
        '''
        
        '''
        _, msg_id = customer_srv_id_get()
        r = gmhttp.get(self.url.format(msg_id)).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data', r.keys())
        self.assertIn('user_safe_toast', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('user_safe_toast'), str)
        self.assertIn('target_doctor_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('target_doctor_id'), str)
        self.assertIn('target_hospital_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('target_hospital_id'), str)
        self.assertIn('custom_service_phone', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('custom_service_phone'), str)
        self.assertIn('conversation_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('conversation_id'), int)
        self.assertIn('results', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('results'), list)
        self.assertIn('target_uid', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('target_uid'), int)
        self.assertIn('nickname', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('nickname'), str)
        self.assertIn('is_new', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_new'), int)
        self.assertIn('target_type', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('target_type'), int)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Conversation_Detail_User_Key.run()
