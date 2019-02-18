import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Verification_Code(unittest.TestCase):
    '''
    验证码接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_verification_code")))
    def test_verification_code(self,value):
        self._testMethodDoc = "--"
        '''
        验证码接口
        '''
        post_data = {'phone': '+8611123456789', 'type':	'4', 'verifier': '34ab65f4d810ef2d2bfab590d4148182'}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])



    def tearDown(self):
        pass


if __name__ == "__main__":
    Verification_Code.run()