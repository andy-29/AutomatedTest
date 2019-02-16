import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Customer_Srv_Is_Direct_Talk(unittest.TestCase):
    '''
    是否可以直接进入客服咨询
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name



    @data(*(get_values(func, "test_customer_srv_is_direct_talk")))
    @require_login
    def test_customer_srv_is_direct_talk(self,value):
        r = gmhttp.get(url=g.host + '/api/customer_srv/is_direct_talk').json()
        self.assertEqual(0, r['error'])
        entry_id = r['data']['entry_id']
        user_key = r['data']['user_key']
        return entry_id, user_key

    def tearDown(self):
        pass


if __name__ == "__main__":
    Customer_Srv_Is_Direct_Talk.run()