import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone_Unfollow(unittest.TestCase):
    '''
    圈子取消关注
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_zone_unfollow")))
    def test_zone_unfollow(self,value):
        '''
        圈子取消关注
        '''
        tag_id, tag_name = zone_my_get()
        post_data = {'tag_id': tag_id, 'tag_name': tag_name}
        r = gmhttp.post(url=self.url, data=post_data).json()

        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_Unfollow.run()