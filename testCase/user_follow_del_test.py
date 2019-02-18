import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Follow_Del(unittest.TestCase):
    '''
    取消关注
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_user_follow_del")))
    @require_login
    def test_user_follow_del(self,value):
        self._testMethodDoc = "--"
        post_data = {'uid': '22'}
        r = gmhttp.post(url=self.url,data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Follow_Del.run()
