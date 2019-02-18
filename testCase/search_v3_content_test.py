import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Search_V3_Content(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_search_v3_content")))
    def test_search_v3_content(self,value):
        self._testMethodDoc = "--"
        '''
        v3综合搜索
        '''
        gmhttp.params.update({"q":"眼"})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('guess_type', r.get('data').keys())
        self.assertIn('features', r.get('data').keys())
        for item in r.get('data').get('features'):
            self.assertIn('type', item.keys())
            self.assertIsInstance(item.get('type'), int)
            self.assertIn('眼',str(item))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Search_V3_Content.run()