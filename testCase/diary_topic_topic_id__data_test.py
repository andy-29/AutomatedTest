import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from  common.id_for_test import diary_id_get
import time
@ddt
class Diary_Topic_Topic_Id__Data(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()


    @data(*(get_values(func, "test_diary_topic_topic_id__data")))
    @require_login
    def test_diary_topic_topic_id__data(self,value):
        '''
        获取日记本信息
        '''
        r = gmhttp.get(self.url.format(self.diary_id)).json()
        self.assertEqual(r.get("error"),0)
        if not r.get('data'):
            data = {
                'tag_ids':'[]',
                'polymer_ids':'[]',
                'topic_list':'[{"content":"测试内容","images":[],"operation_timestamp":%s}]'%str(int(time.time())),
                'zone_tags':'[]'
            }
            url = self.host + g.get_info('api_info','diary_update_v2_diary_id').format(self.diary_id)
            r1 = gmhttp.post(url,verify=False,data=data).json()
            self.assertEqual(r1.get("error"),0)
        #================================
        # 获取第一个日志
        r = gmhttp.get(self.url.format(self.diary_id)).json()
        diary_info = r.get('data')[0]
        self.assertIn('diary_num', diary_info.keys())
        # self.assertIsInstance(item.get('diary_num'), int)
        # self.assertEqual(1,diary_info.get('diary_num'))
        self.assertIn('is_liked', diary_info.keys())
        self.assertIsInstance(diary_info.get('is_liked'), bool)
        self.assertIn('post_date', diary_info.keys())
        self.assertIsInstance(diary_info.get('post_date'), str)
        self.assertIn('reply_count', diary_info.keys())
        self.assertIsInstance(diary_info.get('reply_count'), int)
        self.assertIn('video', diary_info.keys())
        self.assertIsInstance(diary_info.get('video'), dict)
        self.assertIn('images', diary_info.keys())
        self.assertIsInstance(diary_info.get('images'), list)
        self.assertIn('id', diary_info.keys())
        self.assertIsInstance(diary_info.get('id'), int)
        self.assertIn('view_count', diary_info.keys())
        self.assertIsInstance(diary_info.get('view_count'), int)
        self.assertIn('comments', diary_info.keys())
        self.assertIsInstance(diary_info.get('comments'), list)
        self.assertIn('operation_day', diary_info.keys())
        self.assertIsInstance(diary_info.get('operation_day'), str)
        self.assertIn('content', diary_info.keys())
        # self.assertEqual('测试内容',diary_info.get('content'))
        self.assertIn('vote_count', diary_info.keys())
        self.assertIsInstance(diary_info.get('vote_count'), int)
        self.assertIn('replay', diary_info.keys())
        self.assertIsInstance(diary_info.get('replay'), dict)
        self.assertIn('is_fake_operation_time', diary_info.keys())
        self.assertIsInstance(diary_info.get('is_fake_operation_time'), bool)
        print('用例执行完毕!')


    def tearDown(self):
        pass



if __name__ == "__main__":
    Diary_Topic_Topic_Id__Data.run()