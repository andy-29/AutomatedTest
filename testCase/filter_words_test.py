import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Filter_Words(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_filter_words")))
    def test_filter_words(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        r = gmhttp.get(self.url).json()
        self.assertIn('words',r.keys())
        self.assertIsInstance(r.get('words'),list)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Filter_Words.run()