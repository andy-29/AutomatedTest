import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Preview(unittest.TestCase):
    '''
    买单页面
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_maidan_preview")))
    @require_login
    def test_maidan_preview(self,value):
        '''
        买单页面
        '''
        *_,doctor_id,_ = service_id_get()

        gmhttp.params.update({"doctor_id":doctor_id})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Preview.run()