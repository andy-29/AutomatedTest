import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Maidan_Create(unittest.TestCase):
    '''
    买单提交
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_maidan_create")))
    @require_login
    def test_maidan_create(self,value):
        self._testMethodDoc = "--"
        '''
        买单提交
        '''
        *_,doctor_id,_ = service_id_get()
        data = {
            'tag_ids':"[0]",
            "payment":0,
            "doctor_id":doctor_id
        }
        r = gmhttp.post(url=self.url,data=data).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Create.run()
