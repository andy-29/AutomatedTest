import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Community_Suozhang_Column(unittest.TestCase):
    '''
    所长说列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_community_suozhang_column")))
    def test_community_suozhang_column(self,value):
        '''
        所长说列表页
        '''
        self._testMethodDoc = '所长说列表页'
        r = gmhttp.get(self.url)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        for item in r.get('data'):
            self.assertIn('date',item.keys())
            self.assertIn('url',item.keys())
            self.assertIn('banner',item.keys())
            self.assertIn('id',item.keys())
            self.assertIn('title',item.keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Community_Suozhang_Column.run()