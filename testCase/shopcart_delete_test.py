import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Shopcart_Delete(unittest.TestCase):
    '''
    删除购物车内容
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_shopcart_delete")))
    @require_login
    def test_shopcart_delete(self, value):
        self._testMethodDoc = "--"
        myid = shopcart_info_get()[0]
        if myid:
            post_data = {'id': myid}  # 5312
            r = gmhttp.post(url=self.url, data=post_data).json()
            self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Shopcart_Delete.run()
