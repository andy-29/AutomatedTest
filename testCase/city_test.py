import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class City(unittest.TestCase):
    '''
    选择邮寄地址城市列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
    @data(*(get_values(func, "test_city")))
    def test_city(self,value):
        '''
        选择邮寄地址城市列表
        '''
        self._testMethodDoc = '选择邮寄地址城市列表'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r,value.get('assertdata'))

    def tearDown(self):
        pass


if __name__ == "__main__":
    City.run()