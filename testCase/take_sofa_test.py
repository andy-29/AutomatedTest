import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Take_Sofa(unittest.TestCase):
    '''
    抢沙发页面
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_take_sofa")))
    @require_login
    def test_take_sofa(self,value):
        self._testMethodDoc = "--"
        '''
        抢沙发页面
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        for item in r.get('data'):
            self.assertIn('title_style_type', item.keys())
            self.assertIsInstance(item.get('title_style_type'), str)
            self.assertIn('reply_num', item.keys())
            self.assertIsInstance(item.get('reply_num'), int)
            self.assertIn('uname', item.keys())
            self.assertIsInstance(item.get('uname'), str)
            self.assertIn('city', item.keys())
            self.assertIsInstance(item.get('city'), (type(None),str))
            self.assertIn('user_id', item.keys())
            self.assertIsInstance(item.get('user_id'), int)
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('is_voted', item.keys())
            self.assertIsInstance(item.get('is_voted'), bool)
            self.assertIn('patient_image_thumb', item.keys())
            self.assertIsInstance(item.get('patient_image_thumb'), str)
            self.assertIn('vote_num', item.keys())
            self.assertIsInstance(item.get('vote_num'), int)
            self.assertIn('live', item.keys())
            self.assertIsInstance(item.get('live'), dict)
            self.assertIn('user_name', item.keys())
            self.assertIsInstance(item.get('user_name'), str)
            self.assertIn('author_type', item.keys())
            self.assertIsInstance(item.get('author_type'), str)
            self.assertIn('content_type', item.keys())
            self.assertIsInstance(item.get('content_type'), str)
            self.assertIn('is_private', item.keys())
            self.assertIsInstance(item.get('is_private'), bool)
            self.assertIn('view_num', item.keys())
            self.assertIsInstance(item.get('view_num'), int)
            self.assertIn('reason_jump', item.keys())
            self.assertIsInstance(item.get('reason_jump'), str)
            self.assertIn('doctor_image', item.keys())
            self.assertIsInstance(item.get('doctor_image'), str)
            self.assertIn('is_topic', item.keys())
            self.assertIsInstance(item.get('is_topic'), bool)
            self.assertIn('uid', item.keys())
            self.assertIsInstance(item.get('uid'), int)
            self.assertIn('video_url', item.keys())
            self.assertIsInstance(item.get('video_url'), str)
            self.assertIn('is_recommend', item.keys())
            self.assertIsInstance(item.get('is_recommend'), bool)
            self.assertIn('doctor_name', item.keys())
            self.assertIsInstance(item.get('doctor_name'), str)
            self.assertIn('is_following', item.keys())
            self.assertIsInstance(item.get('is_following'), bool)
            self.assertIn('doctor_num', item.keys())
            self.assertIsInstance(item.get('doctor_num'), int)
            self.assertIn('images', item.keys())
            self.assertIsInstance(item.get('images'), list)
            self.assertIn('portrait', item.keys())
            self.assertIsInstance(item.get('portrait'), str)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('pre_operation_images', item.keys())
            self.assertIsInstance(item.get('pre_operation_images'), list)
            self.assertIn('is_favord', item.keys())
            self.assertIsInstance(item.get('is_favord'), bool)
            self.assertIn('tip', item.keys())
            self.assertIsInstance(item.get('tip'), str)
            self.assertIn('comments', item.keys())
            self.assertIsInstance(item.get('comments'), list)
            self.assertIn('content', item.keys())
            self.assertIsInstance(item.get('content'), str)
            self.assertIn('show_large_images', item.keys())
            self.assertIsInstance(item.get('show_large_images'), bool)
            self.assertIn('patient_image', item.keys())
            self.assertIsInstance(item.get('patient_image'), str)
            self.assertIn('tags', item.keys())
            self.assertIsInstance(item.get('tags'), list)
            self.assertIn('operation_record', item.keys())
            self.assertIsInstance(item.get('operation_record'), str)
            self.assertIn('is_recommend_all', item.keys())
            self.assertIsInstance(item.get('is_recommend_all'), bool)
            self.assertIn('topic_type', item.keys())
            self.assertIsInstance(item.get('topic_type'), str)
            self.assertIn('date', item.keys())
            self.assertIsInstance(item.get('date'), str)
            self.assertIn('video_cover', item.keys())
            self.assertIsInstance(item.get('video_cover'), str)
            self.assertIn('membership_level', item.keys())
            self.assertIsInstance(item.get('membership_level'), str)
            self.assertIn('interval', item.keys())
            self.assertIsInstance(item.get('interval'), str)
            self.assertIn('reason', item.keys())
            self.assertIsInstance(item.get('reason'), str)
            self.assertIn('user_level', item.keys())
            self.assertIsInstance(item.get('user_level'), dict)
            self.assertIn('doctor_id', item.keys())
            self.assertIsInstance(item.get('doctor_id'), str)
            self.assertIn('status_text', item.keys())
            self.assertIsInstance(item.get('status_text'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Take_Sofa.run()