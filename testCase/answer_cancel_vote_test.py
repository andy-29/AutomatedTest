import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Answer_Cancel_Vote(unittest.TestCase):
    '''
    回答取消点赞
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_answer_cancel_vote")))
    @require_login
    def test_answer_cancel_vote(self,value):
        """个人中心，我的话题，取消赞"""

        self._testMethodDoc = '发现-话题详情-回复详情页'

        try:
            gmhttp.post(url=g.host + '/api/answer/vote', data=value.get('requestdata')).json()
        except:
            pass
        r = gmhttp.post(url=g.host + '/api/answer/cancel_vote', data=value.get('requestdata')).json()
        self.assertEqual(r, value.get('assertdata'))


    def tearDown(self):
        pass


if __name__ == "__main__":
    Answer_Cancel_Vote.run()