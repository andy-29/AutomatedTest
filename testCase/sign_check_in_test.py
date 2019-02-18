import gmhttp
import unittest
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys,hashlib,datetime
sys.path.append(BASE_DIR)
from common.get_config import g





import os,sys
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
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

        self.user_telephone = g.get_info('user_info', 'telephone')
        self.password = g.get_info('user_info', 'password')
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')
    @data(*(get_values(func, "test_sign_check_in")))
    def test_sign_check_in(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''

        signdata = hashlib.md5((g.get_info('env_info','sign_salt')+str(datetime.date.today())).encode()).hexdigest()

        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,headers=self.header,data={'sign_date':signdata})
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('status', r.get('data').keys())
        self.assertIn(r.get('data').get('status'), (1,2,3))  #脚本一天执行次数较多，该处不做等值判断
        self.assertIn('float_window', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('float_window'), bool)
        self.assertIn('time', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('time'), str)
        self.assertIn('msg', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('msg'), str)
        self.assertIn('sign_status', r.get('data').keys())
        self.assertTrue(r.get('data').get('sign_status'))

        '''每天只能签到一次，再次签到'''
        signdata = hashlib.md5((g.get_info('env_info','sign_salt')+str(datetime.date.today())).encode()).hexdigest()
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,headers=self.header,data={'sign_date':signdata})
        r=r.json()
        self.assertEqual(r.get('data').get('status'), 2)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Sign_Check_In.run()