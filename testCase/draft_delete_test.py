import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *

@ddt
class Draft_Delete(unittest.TestCase):
    '''
    删除草稿
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


        cls.draft_id = draft_id_get()


    @data(*(get_values(func, "test_draft_delete")))
    def test_draft_delete(self,value):
        self._testMethodDoc = "--"
        '''
        删除草稿
        '''
        r = gmhttp.post(self.url, data = {'draft_id': self.draft_id}).json()
        self.assertEqual(r.get("error"), 0)
        self.assertEqual('草稿已删除', r.get('message'))
        print('用例执行完毕!')

    def tearDown(self):
        # 删除日记本
        pass


if __name__ == "__main__":
    Draft_Delete.run()
