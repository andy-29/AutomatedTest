import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Customer_Srv_Status_Query(unittest.TestCase):
    '''
    轮训客服状态
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_customer_srv_status_query")))
    @require_login
    def test_customer_srv_status_query(self,value):
        '''
        轮训客服状态
        '''
        self._testMethodDoc = '轮训客服状态'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('servant_online', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('servant_online'), bool)
        self.assertIn('people_in_queue', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('people_in_queue'), int)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Customer_Srv_Status_Query.run()