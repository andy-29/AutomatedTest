import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Search_Default_Keywords(unittest.TestCase):
    '''
    默认搜索词
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_search_default_keywords")))
    def test_search_default_keywords(self,value):
        '''
        默认搜索词
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('search_placeholder',r.get('data').keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Search_Default_Keywords.run()