import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Status(unittest.TestCase):
    '''
    获取我的买单数量
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_maidan_status")))
    @require_login
    def test_maidan_status(self,value):
        self._testMethodDoc = "--"
        '''
        获取我的买单数量
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('not_paid', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('not_paid'), int)
        self.assertIn('paid', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('paid'), int)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Status.run()