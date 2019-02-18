import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Settlement_Buy_Again(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_settlement_buy_again")))
    @require_login
    def test_settlement_buy_again(self,value):
        '''
        
        '''
        self.st_id = settlement_id_get()
        post_data = {'buy_left': '0', 'id':	self.st_id}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        #取消订单，防止占用sku数量
        url = self.host + g.get_info('api_info','settlement_delete')
        data = {
            "id":self.st_id,
            "cancel_reason_value":2
        }
        gmhttp.post(url=url, data=data).json()


if __name__ == "__main__":
    Settlement_Buy_Again.run()