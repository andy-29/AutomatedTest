import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import customer_srv_id_get
@ddt
class Conversation_Delta_Message_Detail(unittest.TestCase):
    '''
    增量获取私信/客服接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_conversation_delta_message_detail")))
    @require_login
    def test_conversation_delta_message_detail(self,value):
        '''
        增量获取私信/客服接口
        '''
        _,msg_id = customer_srv_id_get()
        r = gmhttp.get(url=g.host + '/api/conversation/delta_message_detail/' + msg_id).json()
        # pprint(dict_json)
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Conversation_Delta_Message_Detail.run()