import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Sign_Check_In(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.activity_id, _, cls.sign_status, cls.total_days = sign_activity_id_get()

    @data(*(get_values(func, "test_sign_check_in")))
    @require_login
    def test_sign_check_in(self, value):
        self._testMethodDoc = "签到"
        data = {
            'sign_type': 2 if self.sign_status == 2 else 1,
            'activity_id': self.activity_id
        }
        r = gmhttp.post(self.url, data=data).json()
        self.assertIsInstance(r.get("error"), int)

    def tearDown(self):
        pass


if __name__ == "__main__":
    Sign_Check_In.run()
