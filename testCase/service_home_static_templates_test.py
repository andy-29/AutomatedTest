import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Home_Static_Templates(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_service_home_static_templates")))
    def test_service_home_static_templates(self,value):
        '''
        
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('static_templates', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('static_templates'), list)
        for item in r.get('data').get('static_templates'):
            self.assertIn('type', item.keys())
            self.assertIsInstance(item.get('type'), int)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
        self.assertIn('servicetab_badge_index', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('servicetab_badge_index'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Home_Static_Templates.run()