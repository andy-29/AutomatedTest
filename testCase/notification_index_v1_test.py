import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Notification_Index_V1(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_notification_index_v1")))
    def test_notification_index_v1(self,value):
        '''
        
        '''
        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Notification_Index_V1.run()