import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class My_Diary(unittest.TestCase):
    """个人中心日记本进入"""
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        pass

    def tearDown(self):
        pass

    @data(*(get_values(func, "test_my_diary")))
    @require_login
    def test_my_diary(self,value):
        self._testMethodDoc = "--"
        '查看我得日记本'
        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'],msg=r)


if __name__ == '__main__':
    My_Diary.run()
