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
        *_,cls.d_id,_ = service_id_get()
        cls.user_id = uid_get()

    @data(*(get_values(func, "test_conversation_delta_message_detail_user_key")))
    @require_login
    def test_conversation_delta_message_detail_user_key(self,value):
        '''
        
        '''
        r = gmhttp.get(self.url.format('{}_{}'.format(self.d_id,self.user_id))).json()
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