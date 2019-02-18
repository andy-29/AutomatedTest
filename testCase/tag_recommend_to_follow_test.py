import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Tag_Recommend_To_Follow(unittest.TestCase):
    '''
    推荐关注的圈子
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_tag_recommend_to_follow")))
    def test_tag_recommend_to_follow(self,value):
        self._testMethodDoc = "--"
        '''
        推荐关注的圈子
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        for item in r.get('data'):
            self.assertIn('icon', item.keys())
            self.assertIsInstance(item.get('icon'), str)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
            self.assertIn('name', item.keys())
            self.assertIsInstance(item.get('name'), str)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Tag_Recommend_To_Follow.run()