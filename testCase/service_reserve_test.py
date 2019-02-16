import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Reserve(unittest.TestCase):
    '''
    美购预定
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.service_id, _, _ = service_id_get()

    @data(*(get_values(func, "test_service_reserve")))
    @require_login
    def test_service_reserve(self,value):
        '''
        美购预定
        '''

        post_data = {'service_id': self.service_id}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Reserve.run()