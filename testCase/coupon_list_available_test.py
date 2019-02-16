import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Coupon_List_Available(unittest.TestCase):
    '''
    可用美券列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_coupon_list_available")))
    @require_login
    def test_coupon_list_available(self, value):
        '''
        可用美券列表页
        '''
        self._testMethodDoc = '可用美券列表页'
        myid, service_item_id, service_id, transparent_key = shopcart_info_get()
        data = {
            'valid_only':1,
            'start_num': 0,
            'service_item_id': service_item_id,
            'number': 1,
            'coupon_type': 1
        }
        r = gmhttp.post(self.url, data=data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Coupon_List_Available.run()
