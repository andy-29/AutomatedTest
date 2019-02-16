import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Push_Registration(unittest.TestCase):
    '''
    极光推送设备注册
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_push_registration")))
    def test_push_registration(self,value):
        '''
        极光推送设备注册
        '''
        data = {"registration_id":g.get_info('body_params','registration_id')}
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        self.assertEqual(r.get("message"),'设备注册成功')
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Push_Registration.run()