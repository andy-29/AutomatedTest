import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Packet_Callback(unittest.TestCase):
    '''
    红包领取回调
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_packet_callback")))
    @require_login
    def test_packet_callback(self,value):
        self._testMethodDoc = "--"
        '''
        红包领取回调
        '''
        import random
        gmhttp.params.update({"opened":random.randint(0,1),"type":random.randint(0,1)})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0,msg=r)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Packet_Callback.run()