import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import answer_id_get


@ddt
class Answer_Vote(unittest.TestCase):
    """个人中心，发布，回复，赞"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_answer_vote")))
    @require_login
    def test_answer_vote(self, value):
        self._testMethodDoc = '个人中心，发布，回复，赞'
        try:
            gmhttp.post(url=g.host + '/api/answer/cancel_vote', data=value.get('requestdata')).json()
        except:
            pass
        r = gmhttp.post(url=g.host + '/api/answer/vote', data=value.get('requestdata')).json()
        self.assertEqual(0, r['error'])


if __name__ == '__main__':
    Answer_Vote.run()
