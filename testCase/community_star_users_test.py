import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Community_Star_Users(unittest.TestCase):
    '''
    达人列表页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_community_star_users")))
    def test_community_star_users(self,value):
        '''
        达人列表页
        '''
        self._testMethodDoc = '达人列表页'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        for item in r.get('data'):
            self.assertIn('username',item.keys())
            self.assertIn('fans_count',item.keys())
            self.assertIn('user_id',item.keys())
            self.assertIn('describe',item.keys())
            self.assertIn('topic_count',item.keys())
            self.assertIn('vote_count',item.keys())
            self.assertIn('is_following',item.keys())
            self.assertIn('portrait',item.keys())
            self.assertIn('membership_level',item.keys())
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Community_Star_Users.run()