import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Cancel(unittest.TestCase):
    '''
    买单订单取消
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_maidan_cancel")))
    @require_login
    def test_maidan_cancel(self,value):
        self._testMethodDoc = "--"
        '''
        买单订单取消
        '''
        maidan_id = maidan_id_get()
        post_data = {'id': maidan_id}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Cancel.run()