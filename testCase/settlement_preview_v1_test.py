import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Settlement_Preview_V1(unittest.TestCase):
    '''
    提交订单页面
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_settlement_preview_v1")))
    @require_login
    def test_settlement_preview_v1(self,value):
        self._testMethodDoc = "--"
        '''
        提交订单页面
        '''
        mytuple = shopcart_info_get()
        #订单相关不在使用动态真是美购和sku，一律使用测试美购

        post_data = {'cart_item_info':'[ { "id" :' + mytuple[0] + ',"service_item_id" :' + mytuple[1] + ', "number" : 1 } ]'}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Settlement_Preview_V1.run()