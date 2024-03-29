import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Order_Refund_Order_Id(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.order_id,_ = order_settlement_id_get()

    @data(*(get_values(func, "test_order_refund_order_id")))
    @require_login
    def test_order_refund_order_id(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        r = gmhttp.get(self.url.format(self.order_id)).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Order_Refund_Order_Id.run()