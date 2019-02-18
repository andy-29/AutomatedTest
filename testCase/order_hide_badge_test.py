import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Order_Hide_Badge(unittest.TestCase):
    '''
    消除个人主页已付款和已使用的红点
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_order_hide_badge")))
    @require_login
    def test_order_hide_badge(self,value):
        '''
        消除个人主页已付款和已使用的红点
        '''
        data= {
            "status":1
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('updated', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('updated'), bool)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Order_Hide_Badge.run()