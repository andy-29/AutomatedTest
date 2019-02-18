import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Votes_Received(unittest.TestCase):
    '''
    我收到得赞
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_votes_received")))
    @require_login
    def test_votes_received(self,value):
        self._testMethodDoc = "--"
        '''
        我收到得赞
        '''

        r = gmhttp.get(url=self.url).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Votes_Received.run()