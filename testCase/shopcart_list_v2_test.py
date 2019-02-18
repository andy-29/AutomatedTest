import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from copy import deepcopy
@ddt
class Shopcart_List_V2(unittest.TestCase):
    '''
    购物车列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_shopcart_list_v2")))
    @require_login
    def test_shopcart_list_v2(self,value):
        self._testMethodDoc = "--"
        gmhttp.params.update({'count_only':0})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Shopcart_List_V2.run()