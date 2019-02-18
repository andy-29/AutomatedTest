import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Topic_Has_Draft(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_topic_has_draft")))
    def test_topic_has_draft(self,value):
        self._testMethodDoc = "--"
        '''
        日志下是否有草稿
        '''
        gmhttp.params.update({"diary_id":self.diary_id,"type":1})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertIsInstance(r.get('data').get('has_draft'),bool)


    def tearDown(self):
        #删除日记本
        pass


if __name__ == "__main__":
    Topic_Has_Draft.run()