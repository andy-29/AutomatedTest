import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone(unittest.TestCase):
    '''
    圈子列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_zone")))
    def test_zone(self,value):
        self._testMethodDoc = "--"
        '''
        圈子列表页
        '''
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.get(url, verify=False)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone.run()