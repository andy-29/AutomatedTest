import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class Accounts_Logout(unittest.TestCase):
    '''
    登出接口
    '''

    def setUp(self):
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(func)
        self.url = self.host + self.api_name

    @data(*(get_values(func,"test_accounts_logout")))
    @require_login
    def test_accounts_logout(self,value):
        self._testMethodDoc = '成功退出'
        r = gmhttp.post(self.url).json()
        self.assertEqual(r, value.get('assertdata'))
        gmhttp.headers.pop("Cookie")


    def tearDown(self):
        # 强制执行再次登陆，方便后面脚本执行
        # gmhttp.login()
        pass

if __name__ == "__main__":
    Accounts_Logout.run()
