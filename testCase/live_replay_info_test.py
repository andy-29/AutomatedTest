import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Live_Replay_Info(unittest.TestCase):
    '''
    回放信息
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_live_replay_info")))
    @require_login
    def test_live_replay_info(self,value):
        '''
        回放信息
        '''
        # 获取topic列表
        uri = g.get_info('api_info', 'live_list')
        url =self.host + uri
        r = gmhttp.get(url).json()
        self.assertEqual(r.get("error"), 0)
        topic_list =map(lambda x:x.get('topic_id'),filter(lambda x:x.get('status')==0,r.get('data')))

        for topic_id in topic_list:
            gmhttp.params.update({"topic_id":topic_id})
            r = gmhttp.get(self.url).json()
            gmhttp.reset()
            self.assertEqual(r.get("error"), 0)
            self.assertIn('data', r.keys())
            self.assertIn('is_doctor', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('is_doctor'), bool)
            self.assertIn('uname', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('uname'), str)
            self.assertIn('stream_id', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('stream_id'), int)
            self.assertIn('is_following', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('is_following'), bool)
            self.assertIn('show_hospital', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('show_hospital'), bool)
            self.assertIn('share_data', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('share_data'), dict)
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
            self.assertIsInstance(r.get('data').get('id'), int)
            self.assertIn('show_service', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('show_service'), bool)
            self.assertIn('user_id', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('user_id'), int)
            self.assertIn('service', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('service'), dict)
            self.assertIn('title', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('title'), str)
            self.assertIn('user_portrait', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('user_portrait'), str)
            self.assertIn('hospital', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('hospital'), dict)
            self.assertIn('topic_id', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('topic_id'), int)
            self.assertIn('status', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('status'), int)
            self.assertIn('tags', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('tags'), list)
            for item in r.get('data').get('tags'):
                self.assertIn('name', item.keys())
                self.assertIsInstance(item.get('name'), str)
                self.assertIn('tag_id', item.keys())
                self.assertIsInstance(item.get('tag_id'), int)
            self.assertIn('cover_url', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('cover_url'), str)
            self.assertIn('membership_level', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('membership_level'), str)
            self.assertIn('m_url', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('m_url'), str)
            self.assertIn('audience_num', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('audience_num'), str)
            self.assertIn('url', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('url'), str)
            self.assertIn('channel_id', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('channel_id'), int)
            self.assertIn('user_level', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('user_level'), dict)
            self.assertIn('level_icon', r.get('data').get('user_level').keys())
            self.assertIsInstance(r.get('data').get('user_level').get('level_icon'), str)
            self.assertIn('constellation_icon', r.get('data').get('user_level').keys())
            self.assertIsInstance(r.get('data').get('user_level').get('constellation_icon'), str)
            self.assertIn('membership_icon', r.get('data').get('user_level').keys())
            self.assertIsInstance(r.get('data').get('user_level').get('membership_icon'), str)
            break
        print('用例执行完毕!')

    def tearDown(self):
        pass
        #关掉直播
        # finish_zb = g.get_info('api_info','live_finish')
        # url = self.host + finish_zb+ "?" + self.android_params
        # r = gmhttp.post(url,verify=False,headers=self.header,data={"channel_id":self.channel})
        # self.assertEqual(r.status_code,200,'返回码不为200！')
        # r = r.json()
        # self.assertEqual(r.get("error"),0)



if __name__ == "__main__":
    Live_Replay_Info.run()
