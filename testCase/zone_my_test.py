import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone_My(unittest.TestCase):
    '''
    个人中心我的圈子列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_zone_my")))
    @require_login
    def test_zone_my(self,value):
        self._testMethodDoc = "--"
        '我的圈子列表'
        zone_my_get()


    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_My.run()