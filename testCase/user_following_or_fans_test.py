import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Follow_Fans(unittest.TestCase):
    """个人中心，我的关注，用户"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_follow_fans")))
    @require_login
    def test_follow_fans(self,value):
        uid = uid_get()
        inner_data = {}
        inner_data['type'] = 'following'
        inner_data['uid'] = uid
        gmhttp.params.update(inner_data)
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])


if __name__ == "__main__":
    Follow_Fans.run()
