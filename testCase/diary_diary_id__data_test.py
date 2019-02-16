import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Diary_Diary_Id__Data(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_diary_diary_id__data")))
    def test_diary_diary_id__data(self,value):
        '''
        
        '''
        r = gmhttp.get(self.url.format(self.diary_id)).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data', r.keys())
        self.assertIn('favord_count', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('favord_count'), int)
        self.assertIn('jump_content', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('jump_content'), dict)
        self.assertIn('url', r.get('data').get('jump_content').keys())
        self.assertIsInstance(r.get('data').get('jump_content').get('url'), str)
        # self.assertIn('icon', r.get('data').get('jump_content').keys())
        # self.assertIsInstance(r.get('data').get('jump_content').get('icon'), str)
        self.assertIn('title', r.get('data').get('jump_content').keys())
        self.assertIsInstance(r.get('data').get('jump_content').get('title'), str)
        self.assertIn('is_favored', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_favored'), bool)
        self.assertIn('polymer_data', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('polymer_data'), dict)
        self.assertIn('reply_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('reply_num'), int)
        self.assertIn('is_following', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_following'), bool)
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
        self.assertIn('pre_operation_image_amount', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('pre_operation_image_amount'), int)
        self.assertIn('is_login', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_login'), bool)
        self.assertIn('title', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('title'), str)
        self.assertIn('is_voted', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('is_voted'), bool)
        self.assertIn('vote_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('vote_num'), int)
        self.assertIn('post_img', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('post_img'), dict)
        self.assertIn('share_tag', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('share_tag'), dict)
        self.assertIn('type', r.get('data').get('share_tag').keys())
        self.assertIsInstance(r.get('data').get('share_tag').get('type'), str)
        # self.assertIn('id', r.get('data').get('share_tag').keys())
        # self.assertIsInstance(r.get('data').get('share_tag').get('id'), int)
        self.assertIn('tag_id', r.get('data').get('share_tag').keys())
        # self.assertIsInstance(r.get('data').get('share_tag').get('tag_id'), int)
        self.assertIn('name', r.get('data').get('share_tag').keys())
        # self.assertIsInstance(r.get('data').get('share_tag').get('name'), str)
        self.assertIn('topic_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('topic_num'), int)
        self.assertIn('share_count', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('share_count'), int)
        self.assertIn('config', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('config'), dict)
        self.assertIn('host_url', r.get('data').get('config').keys())
        self.assertIsInstance(r.get('data').get('config').get('host_url'), str)
        self.assertIn('url_base', r.get('data').get('config').keys())
        self.assertIsInstance(r.get('data').get('config').get('url_base'), str)
        self.assertIn('tag_data', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('tag_data'), dict)
        self.assertIn('tag_name', r.get('data').get('tag_data').keys())
        self.assertIsInstance(r.get('data').get('tag_data').get('tag_name'), str)
        self.assertIn('tag_id', r.get('data').get('tag_data').keys())
        self.assertIsInstance(r.get('data').get('tag_data').get('tag_id'), int)
        self.assertIn('order_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('order_id'), type(None))
        self.assertIn('baike_tags', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('baike_tags'), list)
        for item in r.get('data').get('baike_tags'):
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('is_hot', item.keys())
            self.assertIsInstance(item.get('is_hot'), bool)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('other_name', item.keys())
            self.assertIsInstance(item.get('other_name'), str)
            self.assertIn('icon', item.keys())
            self.assertIsInstance(item.get('icon'), str)
        self.assertIn('pre_img', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('pre_img'), list)
        self.assertIn('group_diary_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('group_diary_num'), int)
        self.assertIn('author', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('author'), dict)
        self.assertIn('diary_count', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('diary_count'), int)
        self.assertIn('level_icon', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('level_icon'), str)
        self.assertIn('user_portrait', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('user_portrait'), str)
        self.assertIn('is_author', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('is_author'), bool)
        self.assertIn('nickname', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('nickname'), str)
        self.assertIn('id', r.get('data').get('author').keys())
        self.assertIsInstance(r.get('data').get('author').get('id'), int)
        self.assertIn('view_num', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('view_num'), str)
        self.assertIn('service_data', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_data'), dict)
        self.assertIn('id', r.get('data').get('service_data').keys())
        self.assertIsInstance(r.get('data').get('service_data').get('id'), type(None))
        self.assertIn('service_id', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('service_id'), type(None))
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Diary_Id__Data.run()