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
class Live_List(unittest.TestCase):
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


    @data(*(get_values(func, "test_live_list")))
    def test_live_list(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        # url = self.host + self.api_name+ "?" + self.android_params
        url = self.host + self.api_name+ "?" + self.android_params
        r = gmhttp.get(url,verify=False)
        self.assertEqual(r.status_code,200,'返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertGreater(len(r.get('data')),0)
        for item in r.get('data'):
            self.assertIn('uname', item.keys())
            self.assertIsInstance(item.get('uname'), str)
            self.assertIn('stream_id', item.keys())
            self.assertIsInstance(item.get('stream_id'), int)
            self.assertIn('is_following', item.keys())
            self.assertIsInstance(item.get('is_following'), bool)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('user_id', item.keys())
            self.assertIsInstance(item.get('user_id'), int)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('user_portrait', item.keys())
            self.assertIsInstance(item.get('user_portrait'), str)
            # self.assertIn('topic_id', item.keys())
            # self.assertIsInstance(item.get('topic_id'), (type(None),int))
            # self.assertIn('person_id', item.keys())
            # self.assertIsInstance(item.get('person_id'), str)
            self.assertIn('status', item.keys())
            self.assertIsInstance(item.get('status'), int)
            self.assertIn('tags', item.keys())
            self.assertIsInstance(item.get('tags'), list)
            # self.assertIn('topic_view_num', item.keys())
            # self.assertIsInstance(item.get('topic_view_num'), int)
            self.assertIn('cover_url', item.keys())
            self.assertIsInstance(item.get('cover_url'), str)
            self.assertIn('membership_level', item.keys())
            self.assertIsInstance(item.get('membership_level'), str)
            # self.assertIn('m_url', item.keys())
            # self.assertIsInstance(item.get('m_url'), str)
            self.assertIn('audience_num', item.keys())
            self.assertIsInstance(item.get('audience_num'), (str,int))
            self.assertIn('url', item.keys())
            self.assertIsInstance(item.get('url'), str)
            # self.assertIn('hospital_id', item.keys())
            # self.assertIsInstance(item.get('hospital_id'), str)
            # self.assertIn('save_replay_url', item.keys())
            # self.assertIsInstance(item.get('save_replay_url'), str)
            self.assertIn('channel_id', item.keys())
            self.assertIsInstance(item.get('channel_id'), int)
            self.assertIn('user_level', item.keys())
            self.assertIsInstance(item.get('user_level'), dict)
            # self.assertIn('service_id', item.keys())
            # self.assertIsInstance(item.get('service_id'), str)
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
    Live_List.run()