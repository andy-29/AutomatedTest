import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Notification_V1(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_notification_v1")))
    @require_login
    def test_notification_v1(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        gmhttp.params.update({"type":'0'})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Notification_V1.run()