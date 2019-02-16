import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class City_Located(unittest.TestCase):
    '''
    根据经纬度获取城市，当前仅支持国内城市，无法验证西半球和南半球城市
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_city_located_beijing")))
    def test_city_located_beijing(self, value):
        '''
        根据经纬度获取城市
        '''
        self._testMethodDoc = '根据经纬度获取城市-北京'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r,value.get('assertdata'))

    # @data(*(get_values(func, "test_city_located_london")))
    # def test_city_located_london(self,value):
    #     '''
    #     根据经纬度获取城市
    #     '''
    #     url = self.host + self.api_name+ "?" + g.android_params_set(lat=51.5,lng=0)
    #     r = gmhttp.get(url,verify=False)
    #     self.assertEqual(r.status_code,200,'返回码不为200！')
    #     r = r.json()
    #     self.assertEqual(r.get("error"),0)
    #     self.assertIn('data',r.keys())
    #     self.assertEqual('London',r.get('data').get('city_id'))
    #     self.assertEqual('伦敦',r.get('data').get('city_name'))
    #     print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    City_Located.run()
