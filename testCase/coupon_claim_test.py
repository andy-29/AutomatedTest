import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Coupon_Claim(unittest.TestCase):
    '''
    领取美券
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_coupon_claim")))
    @require_login
    def test_coupon_claim(self,value):
        self._testMethodDoc = "--"
        '''
        领取美券
        '''
        r = gmhttp.post(url=g.host + '/api/coupon/claim', data=value.get('requestdata')).json()
        self.assertEqual(11002, r['error_code'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Coupon_Claim.run()