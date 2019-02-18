import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Msg_Reply_Msg(unittest.TestCase):
    '''
    收到的与发出得回复
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_msg_reply_msg")))
    @require_login
    def test_msg_reply_msg_sent(self, value):
        self._testMethodDoc = "--"
        '''
        发出得回复
        '''
        gmhttp.params.update({"type": "sent"})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    @data(*(get_values(func, "test_msg_reply_msg")))
    @require_login
    def test_msg_reply_msg_receive(self, value):
        self._testMethodDoc = "--"
        '''
        收到得回复
        '''
        gmhttp.params.update({"type": "receive"})
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Msg_Reply_Msg.run()
