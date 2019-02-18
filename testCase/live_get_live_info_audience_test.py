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
class Live_Get_Live_Info_Audience(unittest.TestCase):
    '''
    观众获取房间信息
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
    @data(*(get_values(func, "test_live_get_live_info_audience")))
    def test_live_get_live_info_audience(self,value):
        self._testMethodDoc = "--"
        '''
        观众获取房间信息
        '''
        url = self.host + self.api_name+ "?" + self.android_params+'&channel_id={}'.format(self.channel)
        r = gmhttp.get(url,verify=False)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIn('is_doctor', r.get('data').keys())
        self.assertIn('uname', r.get('data').keys())
        self.assertIn('stream_id', r.get('data').keys())
        self.assertIn('is_following', r.get('data').keys())
        self.assertIn('show_hospital', r.get('data').keys())
        self.assertIn('share_data', r.get('data').keys())
        self.assertIn('qq', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('qq'), dict)
        self.assertIn('weibo', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('weibo'), dict)
        self.assertIn('url', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('url'), str)
        self.assertIn('image', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('image'), str)
        self.assertIn('wechatmini', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechatmini'), dict)
        self.assertIn('wechat', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechat'), dict)
        self.assertIn('wechatline', r.get('data').get('share_data').keys())
        self.assertIsInstance(r.get('data').get('share_data').get('wechatline'), dict)
        self.assertIn('id', r.get('data').keys())
        self.assertIn('show_service', r.get('data').keys())
        self.assertIn('user_id', r.get('data').keys())
        self.assertIn('service', r.get('data').keys())
        self.assertIn('title', r.get('data').keys())
        self.assertIn('user_portrait', r.get('data').keys())
        self.assertIn('hospital', r.get('data').keys())
        self.assertIn('status', r.get('data').keys())
        self.assertIn('tags', r.get('data').keys())
        for item in r.get('data').get('tags'):
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('tag_id', item.keys())
            self.assertIsInstance(item.get('tag_id'), int)
        self.assertIn('cover_url', r.get('data').keys())
        self.assertIn('membership_level', r.get('data').keys())
        self.assertIn('m_url', r.get('data').keys())
        self.assertIn('audience_num', r.get('data').keys())
        self.assertIn('url', r.get('data').keys())
        self.assertIn('channel_id', r.get('data').keys())
        self.assertIn('user_level', r.get('data').keys())
        self.assertIn('level_icon', r.get('data').get('user_level').keys())
        self.assertIsInstance(r.get('data').get('user_level').get('level_icon'), str)
        self.assertIn('constellation_icon', r.get('data').get('user_level').keys())
        self.assertIsInstance(r.get('data').get('user_level').get('constellation_icon'), str)
        self.assertIn('membership_icon', r.get('data').get('user_level').keys())
        self.assertIsInstance(r.get('data').get('user_level').get('membership_icon'), str)
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
    Live_Get_Live_Info_Audience.run()