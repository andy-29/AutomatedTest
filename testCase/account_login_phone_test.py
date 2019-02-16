import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class Account_Login_Phone(unittest.TestCase):
    '''
    登入接口
    '''
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    # @data(*(get_values(func, "test_account_login_phone")))
    # def test_account_login_phone(self, value):
    #     self._testMethodDoc = '登入接口，手机号验证码正确'
    #     r = gmhttp.post(self.url, data=value.get("requestdata")).json()
    #     self.assertEqual(r, value.get('assertdata'))

    @data(*(get_values(func, "test_account_login_phone_errorCode")))
    def test_account_login_phone_errorCode(self, value):
        self._testMethodDoc = '手机号码正确，验证码错误'
        r = gmhttp.post(self.url, data=value.get("requestdata")).json()
        self.assertEqual(r, value.get('assertdata'))

    @data(*(get_values(func, "test_account_login_phone_errorTel")))
    def test_account_login_phone_errorTel(self, value):
        self._testMethodDoc = '手机号码错误'
        r = gmhttp.post(self.url, data=value.get("requestdata")).json()
        self.assertEqual(r, value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    Account_Login_Phone.run()
