import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Index_V6(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_index_v6")))
    def test_index_v6(self,value):
        '''
        
        '''
        r = gmhttp.get(self.url,timeout= 10).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('function_area_mutiple', r.get('data').keys())
        # for item in r.get('data').get('function_area_mutiple'):
        #     print(item)
        self.assertIn('slides', r.get('data').keys())
        for item in r.get('data').get('slides'):
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('slide_img', item.keys())
            self.assertIsInstance(item.get('slide_img'), str)
            self.assertIn('slide_url', item.keys())
            self.assertIsInstance(item.get('slide_url'), str)
            self.assertIn('slide_img_big', item.keys())
            self.assertIsInstance(item.get('slide_img_big'), str)
        self.assertIn('features', r.get('data').keys())
        # for item in r.get('data').get('features'):
        #     self.assertIn('diary', item.keys())
        #     self.assertIsInstance(item.get('diary'), dict)
        #     self.assertIn('type', item.keys())
        #     self.assertIsInstance(item.get('type'), str)
        #     self.assertIn('id', item.keys())
        #     self.assertIsInstance(item.get('id'), int)
        #     self.assertIn('__source', item.keys())
        #     self.assertIsInstance(item.get('__source'), str)
        self.assertIn('offset', r.get('data').keys())
        self.assertIn('is_gray', r.get('data').keys())
        self.assertIn('static_templates', r.get('data').keys())
        for item in r.get('data').get('static_templates'):
            self.assertIn('a', item.keys())
            self.assertIsInstance(item.get('a'), dict)
            self.assertIn('type', item.keys())
            self.assertIsInstance(item.get('type'), int)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
        self.assertIn('live_enable', r.get('data').keys())
        self.assertIn('tab_info', r.get('data').keys())
        for item in r.get('data').get('tab_info'):
            self.assertIn('tab_type', item.keys())
            self.assertIsInstance(item.get('tab_type'), (str,int))
            self.assertIn('tab_name', item.keys())
            self.assertIsInstance(item.get('tab_name'), str)
            self.assertIn('content_type', item.keys())
            self.assertIsInstance(item.get('content_type'), int)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Index_V6.run()