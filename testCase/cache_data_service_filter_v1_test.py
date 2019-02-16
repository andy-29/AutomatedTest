import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Cache_Data_Service_Filter_V1(unittest.TestCase):
    '''
    筛选器选择城市
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_cache_data_service_filter_v1")))
    def test_cache_data_service_filter_v1(self,value):
        '''
        筛选器选择城市
        '''
        self._testMethodDoc = '筛选器选择城市'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        #判断每个筛选条件下有值
        self.assertTrue(all(r.get('data').values()))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Cache_Data_Service_Filter_V1.run()