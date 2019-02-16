import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Shopcart_Set_Number(unittest.TestCase):
    '''
    设置购物车项目数量
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_shopcart_set_number")))
    @require_login
    def test_shopcart_set_number(self,value):
        '设置购物车项目数量'
        myId = shopcart_info_get()
        post_data = {'id': myId[0], 'number': '3'}
        r = gmhttp.post(url=self.url,data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Shopcart_Set_Number.run()