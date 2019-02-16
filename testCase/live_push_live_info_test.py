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
class Live_Push_Live_Info(unittest.TestCase):
    '''
    获取推流信息
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
        # 直接使用getcookie的create_header函数，返回内容不为空则此脚本成功
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')

        # 先上传图片,图片放在conmmon下
        url = self.host + '/files/upload/' + "?" + self.android_params
        with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
            info = f.read()
        files = {"file": ('test.jpg', info, 'image/jpg')}
        r = gmhttp.post(url, files=files, headers=self.header, verify=False)
        self.assertEqual(200, r.status_code)
        self.file_name = r.json().get('data').get('file')

    @data(*(get_values(func, "test_live_push_live_info")))
    def test_live_push_live_info(self,value):
        '''
        获取推流信息
        '''
        tag_id = g.get_info('env_info', 'tag_id1')
        url = self.host + self.api_name + "?" + 'title={}&cover_url={}&tag_id={}'.format('直播测试',
                                                                                          self.file_name,
                                                                                          tag_id) + '&'+self.android_params
        r = gmhttp.get(url, verify=False, headers=self.header)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data',r.keys())
        self.assertIn('url', r.get('data').keys())
        self.assertIn('channel', r.get('data').keys())
        print('用例执行完毕!')
        self.channel = r.get('data').get('channel')
    def tearDown(self):
        #关掉直播
        finish_zb = g.get_info('api_info','live_finish')
        url = self.host + finish_zb+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,headers=self.header,data={"channel_id":self.channel})
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)


if __name__ == "__main__":
    Live_Push_Live_Info.run()