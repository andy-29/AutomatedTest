import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Notification_Index(unittest.TestCase):
    '''
    消息-通知首页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_notification_index")))
    def test_notification_index(self,value):
        self._testMethodDoc = "--"
        '''
        消息-通知首页
        '''
        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Notification_Index.run()