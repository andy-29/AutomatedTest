import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Tag_My(unittest.TestCase):
    '''
    返回热门圈子与我的圈子
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_tag_my")))
    @require_login
    def test_tag_my(self,value):
        '''
        返回热门圈子与我的圈子
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"), 0)
        self.assertIn('hot_recommend_tags', r.get('data').keys())
        for item in r.get('data').get('hot_recommend_tags'):
            self.assertIn('is_operation_tag', item.keys())
            self.assertIsInstance(item.get('is_operation_tag'), bool)
            self.assertIn('description', item.keys())
            self.assertIsInstance(item.get('description'), str)
            self.assertIn('tag_type', item.keys())
            self.assertIsInstance(item.get('tag_type'), str)
            self.assertIn('has_service', item.keys())
            self.assertIsInstance(item.get('has_service'), bool)
            self.assertIn('tag_id', item.keys())
            self.assertIsInstance(item.get('tag_id'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('banner', item.keys())
            self.assertIsInstance(item.get('banner'), str)
            self.assertIn('has_diary', item.keys())
            self.assertIsInstance(item.get('has_diary'), bool)
            self.assertIn('has_wiki', item.keys())
            self.assertIsInstance(item.get('has_wiki'), bool)
            self.assertIn('is_online', item.keys())
            self.assertIsInstance(item.get('is_online'), bool)
            self.assertIn('free_to_add', item.keys())
            self.assertIsInstance(item.get('free_to_add'), bool)
            self.assertIn('has_zone', item.keys())
            self.assertIsInstance(item.get('has_zone'), bool)
            self.assertIn('icon', item.keys())
            self.assertIsInstance(item.get('icon'), str)
        self.assertIn('my_tags', r.get('data').keys())
        for item in r.get('data').get('my_tags'):
            self.assertIn('is_operation_tag', item.keys())
            self.assertIsInstance(item.get('is_operation_tag'), bool)
            self.assertIn('description', item.keys())
            self.assertIsInstance(item.get('description'), str)
            self.assertIn('tag_type', item.keys())
            self.assertIsInstance(item.get('tag_type'), str)
            self.assertIn('has_service', item.keys())
            self.assertIsInstance(item.get('has_service'), bool)
            self.assertIn('tag_id', item.keys())
            self.assertIsInstance(item.get('tag_id'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
            self.assertIn('banner', item.keys())
            self.assertIsInstance(item.get('banner'), str)
            self.assertIn('has_diary', item.keys())
            self.assertIsInstance(item.get('has_diary'), bool)
            self.assertIn('has_wiki', item.keys())
            self.assertIsInstance(item.get('has_wiki'), bool)
            self.assertIn('is_online', item.keys())
            self.assertIsInstance(item.get('is_online'), bool)
            self.assertIn('free_to_add', item.keys())
            self.assertIsInstance(item.get('free_to_add'), bool)
            self.assertIn('has_zone', item.keys())
            self.assertIsInstance(item.get('has_zone'), bool)
            self.assertIn('icon', item.keys())
            self.assertIsInstance(item.get('icon'), str)

        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Tag_My.run()
