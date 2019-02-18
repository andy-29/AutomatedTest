import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Push_History(unittest.TestCase):
    '''
    用户接受的活动推送
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_push_history")))
    def test_push_history(self,value):
        self._testMethodDoc = "--"
        '''
        用户接受的活动推送
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        for item in r.get('data'):
            self.assertIn('title', item.keys())
            self.assertIsInstance(item.get('title'), str)
            self.assertIn('url', item.keys())
            self.assertIsInstance(item.get('url'), str)
            self.assertIn('date', item.keys())
            self.assertIsInstance(item.get('date'), str)
            self.assertIn('portrait', item.keys())
            self.assertIsInstance(item.get('portrait'), str)
            self.assertIn('banner', item.keys())
            self.assertIsInstance(item.get('banner'), str)
            self.assertIn('id', item.keys())
            self.assertIsInstance(item.get('id'), int)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Push_History.run()