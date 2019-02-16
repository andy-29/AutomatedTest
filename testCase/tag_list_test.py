import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Tag_List(unittest.TestCase):
    """日记本发布"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_tag_list")))
    def test_tag_list(self,value):
        gmhttp.params.update({"level":3,"tag_from":0})
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"), 0)


if __name__ == '__main__':
    Tag_List.run()
