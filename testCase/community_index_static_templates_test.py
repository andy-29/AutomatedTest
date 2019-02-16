import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Community_Index_Static_Templates(unittest.TestCase):
    '''
    首页固定模板区刷新
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_community_index_static_templates")))
    def test_community_index_static_templates(self,value):
        '''
        首页固定模板区刷新
        '''

        r = gmhttp.get(self.url)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('static_templates',r.get('data').keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Community_Index_Static_Templates.run()