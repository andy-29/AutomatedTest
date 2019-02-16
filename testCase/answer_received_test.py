import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Answer_Received(unittest.TestCase):
    '''
    收到的回答
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_answer_received")))
    @require_login
    def test_answer_received(self, value):
        '''
        收到的回答
        '''
        self._testMethodDoc = '收到的回答'
        r = gmhttp.get(url=g.host + '/api/answer/received' ).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Answer_Received.run()
