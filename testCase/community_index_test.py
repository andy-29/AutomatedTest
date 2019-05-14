import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Community_Index(unittest.TestCase):
    '''
    社区首页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_community_index")))
    def test_community_index(self,value):
        '''
        社区首页
        '''
        self._testMethodDoc = '社区首页'
        for num in [0,1,2]:
            gmhttp.params.update({"tabtype":num})
            r = gmhttp.get(self.url).json()
            gmhttp.reset()
            self.assertEqual(r.get("error"),0)
            self.assertIn('data', r.keys())
            self.assertIn('hot_tags', r.get('data').keys())
            # self.assertIsInstance(r.get('data').get('hot_tags'), dict)
            # self.assertIn('tags_url', r.get('data').get('hot_tags').keys())
            # self.assertIsInstance(r.get('data').get('hot_tags').get('tags_url'), str)
            # self.assertIn('tag_list', r.get('data').get('hot_tags').keys())
            # self.assertIsInstance(r.get('data').get('hot_tags').get('tag_list'), list)
            self.assertIn('topics', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('topics'), list)
            if r.get('data').get('topics'):
                for item in r.get('data').get('topics'):
                    self.assertIn('uid', item.keys())
                    self.assertIsInstance(item.get('uid'), int)
                    self.assertIn('video_url', item.keys())
                    self.assertIsInstance(item.get('video_url'), str)
                    self.assertIn('is_recommend', item.keys())
                    self.assertIsInstance(item.get('is_recommend'), bool)
                    self.assertIn('reply_num', item.keys())
                    self.assertIsInstance(item.get('reply_num'), int)
                    self.assertIn('doctor_name', item.keys())
                    self.assertIsInstance(item.get('doctor_name'), str)
                    self.assertIn('uname', item.keys())
                    self.assertIsInstance(item.get('uname'), str)
                    self.assertIn('is_topic', item.keys())
                    self.assertIsInstance(item.get('is_topic'), bool)
                    self.assertIn('doctor_num', item.keys())
                    self.assertIsInstance(item.get('doctor_num'), int)
                    self.assertIn('images', item.keys())
                    self.assertIsInstance(item.get('images'), list)
                    self.assertIn('portrait', item.keys())
                    self.assertIsInstance(item.get('portrait'), str)
                    self.assertIn('id', item.keys())
                    self.assertIsInstance(item.get('id'), int)
                    self.assertIn('city', item.keys())
                    self.assertIsInstance(item.get('city'), (type(None),str))
                    self.assertIn('pre_operation_images', item.keys())
                    self.assertIsInstance(item.get('pre_operation_images'), list)
                    self.assertIn('user_id', item.keys())
                    self.assertIsInstance(item.get('user_id'), int)
                    self.assertIn('title', item.keys())
                    self.assertIsInstance(item.get('title'), str)
                    self.assertIn('is_voted', item.keys())
                    self.assertIsInstance(item.get('is_voted'), bool)
                    self.assertIn('is_favord', item.keys())
                    self.assertIsInstance(item.get('is_favord'), bool)
                    self.assertIn('patient_image_thumb', item.keys())
                    self.assertIsInstance(item.get('patient_image_thumb'), str)
                    self.assertIn('tip', item.keys())
                    self.assertIsInstance(item.get('tip'), str)
                    self.assertIn('vote_num', item.keys())
                    self.assertIsInstance(item.get('vote_num'), int)
                    self.assertIn('comments', item.keys())
                    self.assertIsInstance(item.get('comments'), list)
                    self.assertIn('content', item.keys())
                    self.assertIsInstance(item.get('content'), str)
                    self.assertIn('live', item.keys())
                    self.assertIsInstance(item.get('live'), dict)
                    self.assertIn('video_cover', item.keys())
                    self.assertIsInstance(item.get('video_cover'), str)
                    self.assertIn('show_large_images', item.keys())
                    self.assertIsInstance(item.get('show_large_images'), bool)
                    self.assertIn('patient_image', item.keys())
                    self.assertIsInstance(item.get('patient_image'), str)
                    self.assertIn('user_name', item.keys())
                    self.assertIsInstance(item.get('user_name'), str)
                    self.assertIn('author_type', item.keys())
                    self.assertIsInstance(item.get('author_type'), str)
                    self.assertIn('title_style_type', item.keys())
                    self.assertIsInstance(item.get('title_style_type'), str)
                    self.assertIn('tags', item.keys())
                    self.assertIsInstance(item.get('tags'), list)
                    self.assertIn('operation_record', item.keys())
                    self.assertIsInstance(item.get('operation_record'), str)
                    self.assertIn('is_recommend_all', item.keys())
                    self.assertIsInstance(item.get('is_recommend_all'), bool)
                    self.assertIn('topic_type', item.keys())
                    self.assertIsInstance(item.get('topic_type'), str)
                    self.assertIn('content_type', item.keys())
                    self.assertIsInstance(item.get('content_type'), str)
                    self.assertIn('date', item.keys())
                    self.assertIsInstance(item.get('date'), str)
                    self.assertIn('is_private', item.keys())
                    self.assertIsInstance(item.get('is_private'), bool)
                    self.assertIn('membership_level', item.keys())
                    self.assertIsInstance(item.get('membership_level'), str)
                    self.assertIn('interval', item.keys())
                    self.assertIsInstance(item.get('interval'), str)
                    self.assertIn('reason', item.keys())
                    self.assertIsInstance(item.get('reason'), str)
                    self.assertIn('view_num', item.keys())
                    self.assertIsInstance(item.get('view_num'), int)
                    self.assertIn('reason_jump', item.keys())
                    self.assertIsInstance(item.get('reason_jump'), str)
                    self.assertIn('user_level', item.keys())
                    self.assertIsInstance(item.get('user_level'), dict)
                    self.assertIn('doctor_image', item.keys())
                    self.assertIsInstance(item.get('doctor_image'), str)
                    self.assertIn('is_following', item.keys())
                    self.assertIsInstance(item.get('is_following'), bool)
                    self.assertIn('doctor_id', item.keys())
                    self.assertIsInstance(item.get('doctor_id'), str)
                    self.assertIn('status_text', item.keys())
                    self.assertIsInstance(item.get('status_text'), str)
            self.assertIn('channels', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('channels'), list)
            for item in r.get('data').get('channels'):
                pass
            self.assertIn('selected_qa', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('selected_qa'), list)
            if r.get('data').get('selected_qa'):
                for item in r.get('data').get('selected_qa'):
                    self.assertIn('content', item.keys())
                    self.assertIsInstance(item.get('content'), str)
                    self.assertIn('comment', item.keys())
                    self.assertIsInstance(item.get('comment'), list)
                    self.assertIn('topic_id', item.keys())
                    self.assertIsInstance(item.get('topic_id'), int)
            self.assertIn('hot_activity_tags', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('hot_activity_tags'), dict)
            self.assertIn('tags_url', r.get('data').get('hot_activity_tags').keys())
            self.assertIsInstance(r.get('data').get('hot_activity_tags').get('tags_url'), str)
            self.assertIn('tag_list', r.get('data').get('hot_activity_tags').keys())
            self.assertIsInstance(r.get('data').get('hot_activity_tags').get('tag_list'), list)
            self.assertIn('static_templates', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('static_templates'), list)
            if r.get('data').get('static_templates'):
                for item in r.get('data').get('static_templates'):
                    self.assertIn('a', item.keys())
                    self.assertIsInstance(item.get('a'), dict)
                    self.assertIn('type', item.keys())
                    self.assertIsInstance(item.get('type'), int)
                    self.assertIn('id', item.keys())
                    self.assertIsInstance(item.get('id'), int)
                    self.assertIn('title', item.keys())
                    self.assertIsInstance(item.get('title'), str)
            self.assertIn('topup', r.get('data').keys())
            self.assertIsInstance(r.get('data').get('topup'), list)
            if  r.get('data').get('topup'):
                for item in r.get('data').get('topup'):
                    self.assertIn('url', item.keys())
                    self.assertIsInstance(item.get('url'), str)
                    self.assertIn('title', item.keys())
                    self.assertIsInstance(item.get('title'), str)

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Community_Index.run()