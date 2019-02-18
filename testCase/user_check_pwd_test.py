import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Check_Pwd(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_user_check_pwd")))
    @require_login
    def test_user_check_pwd(self,value):
        self._testMethodDoc = "--"
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertTrue(r.get('data').get('is_reset'))
        print('用例执行完毕!')



    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Check_Pwd.run()