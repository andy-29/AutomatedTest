import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class My_Conversation(unittest.TestCase):
    '''
    我的私信列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_my_conversation")))
    @require_login
    def test_my_conversation(self,value):
        '''
        我的私信列表
        '''
        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    My_Conversation.run()