import gmhttp
import unittest
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(BASE_DIR)
from common.get_config import g





import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Service_Home_V2(unittest.TestCase):
    '''
    美购首页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params
    @data(*(get_values(func, "test_service_home_v2")))
    def test_service_home_v2(self,value):
        self._testMethodDoc = "--"
        '''
        美购首页
        '''
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.get(url,verify=False)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Home_V2.run()