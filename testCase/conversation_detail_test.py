import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import customer_srv_id_get
from copy import deepcopy
from common.common import thirddata

@ddt
class Conversation_Detail(unittest.TestCase):
    '''
    私信详情
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name('conversation_detail_user_key')
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_conversation_detail")))
    def test_conversation_detail(self,value):
        '''
        私信详情
        '''
        _,msg_id = customer_srv_id_get()
        inner_data = deepcopy(data)
        inner_data['last_msg_id'] = thirddata['/api/conversation/detail/']['last_msg_id']
        inner_data['offset_msg_id'] = thirddata['/api/conversation/detail/']['offset_msg_id']
        inner_data['referrer'] = thirddata['/api/conversation/detail/']['referrer']
        inner_data['referrer_id'] = thirddata['/api/conversation/detail/']['referrer_id']
        gmhttp.params.update(inner_data)
        r = gmhttp.get(url=g.host + '/api/conversation/detail/' +msg_id).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Conversation_Detail.run()