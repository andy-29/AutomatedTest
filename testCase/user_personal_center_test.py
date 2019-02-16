import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Personal_Center(unittest.TestCase):
    """请求个人中心"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_peruser_my_topic_testsonal_center")))
    def test_peruser_my_topic_testsonal_center(self, value):
        inner_data = {}
        inner_data.update({'choose_id': '0'})
        inner_data.update({'community_id': '0'})
        gmhttp.params.update(inner_data)
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])


if __name__ == '__main__':
    Personal_Center.run()
