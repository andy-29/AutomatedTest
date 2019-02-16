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
class Slide_Cancel_Vote(unittest.TestCase):
    '''
    首页精选banner取消点赞
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

        data = {
            "banner_id":"1"   #这里取值1，找不到合适的方法获得id
        }
        url = self.host + g.get_info('api_info','slide_vote')+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,data=data,headers = self.header)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        print(r)
        self.assertEqual(r.get("error"),0)
    @data(*(get_values(func, "test_slide_cancel_vote")))
    def test_slide_cancel_vote(self,value):
        '''
        首页精选banner取消点赞
        '''
        data = {
            "banner_id":"2"   #这里取值1，找不到合适的方法获得id
        }
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.get(url,verify=False,data=data,headers=self.header)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Slide_Cancel_Vote.run()