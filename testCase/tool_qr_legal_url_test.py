import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Tool_Qr_Legal_Url(unittest.TestCase):
    '''
    二维码扫描，合法域名
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_tool_qr_legal_url")))
    def test_tool_qr_legal_url(self,value):
        self._testMethodDoc = "--"
        '''
        二维码扫描，合法域名
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Tool_Qr_Legal_Url.run()