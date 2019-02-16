import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Search_V2_Doctor(unittest.TestCase):
    '''
    医生搜索
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_search_v2_doctor")))
    def test_search_v2_doctor(self,value):
        '''
        医生搜索
        '''
        gmhttp.params.update({"q":"鼻"})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        # for item in r.get('data').get('doctors'):
        #     self.assertIn('鼻',str(item))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Search_V2_Doctor.run()