import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Info(unittest.TestCase):
    '''
    个人信息接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_user_info")))
    def test_user_info(self,value):
        self._testMethodDoc = "--"
        uid = uid_get()
        self.assertTrue(uid)


    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Info.run()