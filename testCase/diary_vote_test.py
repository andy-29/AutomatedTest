import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Diary_Vote(unittest.TestCase):
    """
    日记本详情页点赞
    """

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name



    @data(*(get_values(func, "test_diary_vote")))
    @require_login
    def test_diary_vote(self,value):
        self._testMethodDoc = "--"
        """
        日记本详情页点赞
        """
        diary_id = diary_id_others_get()

        post_data = {'diary_id': diary_id}
        try:
            gmhttp.post(url=g.host+g.get_info('api_info','diary_cancel_vote'), data=post_data).json()
        except:
            pass
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Vote.run()
