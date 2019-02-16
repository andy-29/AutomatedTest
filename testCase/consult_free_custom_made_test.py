import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Consult_Free_Custom_Made(unittest.TestCase):
    '''
    免费医美定制
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_consult_free_custom_made")))
    @require_login
    def test_consult_free_custom_made(self,value):
        self._testMethodDoc = '免费医美定制'
        r = gmhttp.get(url=g.host + '/api/consult/free_custom_made').json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Consult_Free_Custom_Made.run()