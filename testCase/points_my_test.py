import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Points_My(unittest.TestCase):
    '''
    个人积分列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_points_my")))
    @require_login
    def test_points_my(self,value):
        '''
        个人积分列表
        '''
        r = gmhttp.get(self.url).json()
        self.assertIn('points_amount',r.keys())
        self.assertIsInstance(r.get('points_amount'),int)
        self.assertIn('history',r.keys())
        self.assertIsInstance(r.get('history'),list)
        if r.get('history'):
            for item in  r.get('history'):
                self.assertIn('reason',item.keys())
                self.assertIn('img_url',item.keys())
                self.assertIn('result',item.keys())
                self.assertIn('operation',item.keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Points_My.run()