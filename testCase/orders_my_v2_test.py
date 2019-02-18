import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Orders_My_V2(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_orders_my_v2")))
    @require_login
    def test_orders_my_v2(self,value):
        self._testMethodDoc = "--"
        """个人中心我的订单接口，未付款已付款是status参数值"""
        status = ['', '0', '1', '2', '3']
        for s in status:
            gmhttp.params.update({"status":s})
            r = gmhttp.get(url=self.url).json()
            gmhttp.reset()
            self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Orders_My_V2.run()