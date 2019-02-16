import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Customer_Srv_Send_Message(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_customer_srv_send_message")))
    @require_login
    def test_customer_srv_send_message(self, value):
        post_data = {'content': '中国'}
        r = gmhttp.post(self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Customer_Srv_Send_Message.run()
