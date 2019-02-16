import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class My_Topic(unittest.TestCase):
    """个人中心，话题，活动贴"""
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_my_topic")))
    @require_login
    def test_my_topic(self,value):
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"), 0)


if __name__ == '__main__':
    My_Topic.run()
