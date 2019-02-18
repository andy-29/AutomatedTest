import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Customer_Srv_Init_Status(unittest.TestCase):
    '''
    进入客服页面后获取初始化状态
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_customer_srv_init_status")))
    @require_login
    def test_customer_srv_init_status(self,value):
        self._testMethodDoc = "--"
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Customer_Srv_Init_Status.run()