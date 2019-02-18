import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Phone_Area_Code(unittest.TestCase):
    '''
    手机获取验证码获取国家手机号区号
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_phone_area_code")))
    def test_phone_area_code(self,value):
        self._testMethodDoc = "--"
        '''
        手机获取验证码获取国家手机号区号
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        for item in r.get('data'):
            self.assertIn('area_name', item.keys())
            self.assertIsInstance(item.get('area_name'), str)
            self.assertIn('area_code', item.keys())
            self.assertIsInstance(item.get('area_code'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Phone_Area_Code.run()