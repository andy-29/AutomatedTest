import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Search_Keywords(unittest.TestCase):
    '''
    搜索词推荐
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_search_keywords")))
    def test_search_keywords(self,value):
        '''
        搜索词推荐
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        for item in r.get("data"):
            self.assertIn("url",item.keys())
            self.assertIn("is_special",item.keys())
            self.assertIn("keyword",item.keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Search_Keywords.run()