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
class Live_Danmu(unittest.TestCase):
    '''
    获取弹幕
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
        #
        # 先上传图片,图片放在conmmon下
        url = self.host + '/files/upload/' + "?" + self.android_params
        with open(os.path.join(BASE_DIR, 'common', 'test.jpg'), 'rb') as f:
            info = f.read()
        files = {"file": ('test.jpg', info, 'image/jpg')}
        r = gmhttp.post(url, files=files, headers=self.header, verify=False)
        self.assertEqual(200, r.status_code)
        self.file_name = r.json().get('data').get('file')

        push_live = g.get_info('api_info','live_push_live_info')
        tag_id = g.get_info('env_info', 'tag_id1')
        url = self.host + push_live + "?" + 'title={}&cover_url={}&tag_id={}'.format('直播测试',
                                                                                          self.file_name,
                                                                                          tag_id) + '&'+self.android_params
        r = gmhttp.get(url, verify=False, headers=self.header)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('data',r.keys())
        self.assertIn('url', r.get('data').keys())
        self.assertIn('channel', r.get('data').keys())
        self.channel = r.get('data').get('channel')

    @data(*(get_values(func, "test_live_danmu")))
    def test_live_danmu(self,value):
        self._testMethodDoc = "--"
        '''
        获取弹幕
        '''
        #发送弹幕----测试服BUG？不发送第一条，会报服务器错误
        import time
        time.sleep(15)  #发送弹幕需要间隔
        uri = g.get_info('api_info', 'live_sendmsg')
        url = self.host + uri + "?" + self.android_params
        data = {"channel_id": self.channel, 'msg': '测试信息1'}
        r = gmhttp.post(url, verify=False, headers=self.header, data=data)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)

        #现获取初始id
        url = self.host + self.api_name+ "?" + self.android_params +'&channel_id={}'.format(self.channel,)
        r = gmhttp.get(url,verify=False)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        _msg_id = r.get('data').get('newest_id')
        time.sleep(15)

        uri = g.get_info('api_info', 'live_sendmsg')
        url = self.host + uri + "?" + self.android_params
        data = {"channel_id": self.channel, 'msg': '测试信息2'}
        r = gmhttp.post(url, verify=False, headers=self.header, data=data)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        self.msg_id = r.get('data').get('id')

        #获取该弹幕
        url = self.host + self.api_name + "?" + self.android_params + '&channel_id={}&msg_id={}'.format(self.channel,
                                                                                                        _msg_id)
        r = gmhttp.get(url,verify=False)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('newest_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('newest_id'), int)
        self.assertIn('news', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('news'), list)
        for item in r.get('data').get('news'):
            self.assertIn('id',item.keys())
            self.assertIn('name',item.keys())
            self.assertIn('text',item.keys())
            self.assertEqual('测试信息2',item.get('text'))
            self.assertIn('type',item.keys())
        self.assertIn('title', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('title'), str)
        self.assertIn('delay', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('delay'), int)
        self.assertIn('audience_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('audience_num'), int)
        print('用例执行完毕!')


    def tearDown(self):
        #关掉直播
        finish_zb = g.get_info('api_info','live_finish')
        url = self.host + finish_zb+ "?" + self.android_params
        r = gmhttp.post(url,verify=False,headers=self.header,data={"channel_id":self.channel})
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)

if __name__ == "__main__":
    Live_Danmu.run()