import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Listing_Notify(unittest.TestCase):
    '''
    设置提醒
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_service_listing_notify")))
    def test_service_listing_notify(self,value):
        self._testMethodDoc = "--"
        '''
        设置提醒
        '''

        post_data = {'diary_id': self.diary_id}
        r = gmhttp.post(self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Listing_Notify.run()