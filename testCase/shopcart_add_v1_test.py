import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Shopcart_Add_V1(unittest.TestCase):
    '''
    加入购物车
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_shopcart_add_v1")))
    @require_login
    def test_shopcart_add_v1(self,value):
        service_item_id = shopcart_info_get()[1]
        post_data = {'number': '1', 'service_item_id': service_item_id}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Shopcart_Add_V1.run()