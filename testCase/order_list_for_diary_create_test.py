import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class List_Diary(unittest.TestCase):
    """创建日记后显示日记列表"""
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_list_diary")))
    @require_login
    def test_list_diary(self,value):
        self._testMethodDoc = "--"
        gmhttp.params.update({"order_id":''})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])


if __name__ == '__main__':
    List_Diary.run()
