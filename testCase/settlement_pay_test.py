import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Settlement_Pay(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_settlement_pay")))
    @require_login
    def test_settlement_pay(self,value):
        '''
        
        '''
        order_id,_ = order_settlement_id_get()
        gmhttp.params.update({"id":order_id})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])



    def tearDown(self):
        pass


if __name__ == "__main__":
    Settlement_Pay.run()