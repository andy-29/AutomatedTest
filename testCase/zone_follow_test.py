import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone_Follow(unittest.TestCase):
    '''
    圈子关注按钮
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_zone_follow")))
    @require_login
    def test_zone_follow(self,value):
        "关注圈子"
        _, zone_id = question_id_get()
        post_data = {'tag_id': zone_id}
        try:
            gmhttp.post(url=g.host + g.get_info('api_info', 'zone_unfollow'),data= post_data)
        except:
            pass
        r = gmhttp.post(self.url,data= post_data).json()
        self.assertEqual(0,r.get('error'))



    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_Follow.run()