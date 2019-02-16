import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Topic_Addview(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.topic_id = live_topic_id_get()


    @data(*(get_values(func, "test_topic_addview")))
    def test_topic_addview(self,value):
        '''
        
        '''

        r = gmhttp.get(self.url.format(self.topic_id)).json()
        self.assertEqual(r.get("error"),0)

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Topic_Addview.run()