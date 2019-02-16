import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class Accounts_Stat(unittest.TestCase):
    '''
    统计新用户接口
    '''
    @classmethod
    def setUpClass(cls):
        print('获取环境信息和接口信息')
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func,"test_accounts_stat")))
    def test_accounts_stat(self,value):
        self._testMethodDoc = '统计新用户接口'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r, value.get('assertdata'))


    def tearDown(self):
        pass


if __name__ == "__main__":
    Accounts_Stat.run()