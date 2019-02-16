import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class User_Hospital_Favor_Hospital_Id(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        _, cls.hospital_id, *_ = service_id_get()

    @data(*(get_values(func, "test_user_hospital_favor_hospital_id_post")))
    @require_login
    def test_user_hospital_favor_hospital_id_post(self, value):
        '''
        设置好感
        '''
        r = gmhttp.post(self.url.format(self.hospital_id)).json()
        self.assertEqual(r.get("error"), 0)

    @data(*(get_values(func, "test_user_hospital_favor_hospital_id_zdelete")))
    @require_login
    def test_user_hospital_favor_hospital_id_zdelete(self, value):
        '''
        删除好感
        '''
        r = gmhttp.delete(self.url.format(self.hospital_id)).json()
        self.assertEqual(r.get("error"), 0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Hospital_Favor_Hospital_Id.run()
