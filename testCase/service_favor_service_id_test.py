import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Favor_Service_Id(unittest.TestCase):
    '''
    收藏
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.service_id,*_ = service_id_get()
    @data(*(get_values(func, "test_service_favor_service_id")))
    @require_login
    def test_service_favor_service_id(self,value):
        '''
        收藏
        '''

        r = gmhttp.post(self.url.format(self.service_id)).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Favor_Service_Id.run()