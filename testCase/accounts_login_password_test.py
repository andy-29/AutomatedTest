import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Accounts_Login_Password(unittest.TestCase):
    '''
    登入接口
    '''

    def setUp(self):
        self.host = g.host
        self.api_name = g.api_name(func)
        self.url = self.host + self.api_name

    @data(*(get_values(func, "test_accounts_login_password")))
    def test_accounts_login_password(self, value):
        self._testMethodDoc = '登入接口'
        r = gmhttp.login()
        self.assertEqual(r, value.get('assertdata'))

    @data(*(get_values(func, "test_accounts_login_password_errorPwd")))
    def test_accounts_login_password_errorPwd(self, value):
        self._testMethodDoc = '账号正确，密码错误'
        user = value.get('requestdata').get('phone')
        pwd = value.get('requestdata').get('password')
        r = gmhttp.login(user,pwd)
        self.assertEqual(r, value.get('assertdata'))

    @data(*(get_values(func, "test_accounts_login_password_errorTel")))
    def test_accounts_login_password_errorTel(self, value):
        self._testMethodDoc = '账号错误'
        user = value.get('requestdata').get('phone')
        pwd = value.get('requestdata').get('password')
        r = gmhttp.login(user,pwd)
        self.assertEqual(r, value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    Accounts_Login_Password.run()
