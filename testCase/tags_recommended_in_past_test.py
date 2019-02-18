import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Tags_Recommended_In_Past(unittest.TestCase):
    '''
    推荐圈子
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_tags_recommended_in_past")))
    def test_tags_recommended_in_past(self,value):
        self._testMethodDoc = "--"
        '''
        推荐圈子
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        for item in r.get('data'):
            self.assertIn('is_operation_tag', item.keys())
            self.assertIsInstance(item.get('is_operation_tag'), bool)
            self.assertIn('latest_reply', item.keys())
            self.assertIsInstance(item.get('latest_reply'), str)
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
    Tags_Recommended_In_Past.run()