import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Consult_Index(unittest.TestCase):
    '''
    咨询首页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_consult_index")))
    def test_consult_index(self,value):
        '''
        咨询首页
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('theme',r.get('data').keys())
        for item in r.get('data').get('theme'):
            self.assertIn('url',item.keys())
            self.assertIn('image',item.keys())
            self.assertIn('desc',item.keys())
            self.assertIn('id',item.keys())
            self.assertIn('title',item.keys())
        self.assertIn('science_knowledge',r.get('data').keys())
        for item in r.get('data').get('science_knowledge'):
            self.assertIn('wiki_url',item.keys())
            self.assertIn('title',item.keys())
            self.assertIn('image',item.keys())
            self.assertIn('wiki_name',item.keys())
            self.assertIn('wiki_id',item.keys())
            self.assertIn('desc',item.keys())
            self.assertIn('wikis',item.keys())
            for sub_item in item.get('wikis'):
                self.assertIn('wiki_id', sub_item.keys())
                self.assertIn('wiki_url', sub_item.keys())
                self.assertIn('wiki_name', sub_item.keys())
        self.assertIn('customization',r.get('data').keys())
        self.assertIn('image',r.get('data').get('customization'))
        self.assertIn('slogan',r.get('data').get('customization'))
        self.assertIn('title',r.get('data').get('customization'))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Consult_Index.run()