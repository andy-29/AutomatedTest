import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Sign_Change_Status(unittest.TestCase):
    '''

    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.activity_id ,cls.status,*_ = sign_activity_id_get()

    @data(*(get_values(func, "test_sign_change_status")))
    @require_login
    def test_sign_change_status(self,value):
        self._testMethodDoc = "更换提醒状态"
        data = {
            'is_remind':1 if self.status == False else 0,
            'activity_id':self.activity_id
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"), 0)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Sign_Change_Status.run()