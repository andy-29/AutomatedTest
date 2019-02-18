import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_City(unittest.TestCase):
    '''
    设置用户城市接口
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_user_city")))
    @require_login
    def test_user_city(self,value):
        self._testMethodDoc = "--"
        '''
        设置用户城市接口
        '''
        data = {
            'city_id':'beijing'
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        self.assertEqual(r.get("message"),'城市信息设置成功')
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    User_City.run()