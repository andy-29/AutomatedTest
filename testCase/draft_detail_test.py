import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Draft_Detail(unittest.TestCase):
    '''
    获取草稿详情
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.draft_id = draft_id_get()

    @data(*(get_values(func, "test_draft_detail")))
    def test_draft_detail(self,value):
        self._testMethodDoc = "--"
        '''
        获取草稿详情
        '''
        gmhttp.params.update({"draft_id":self.draft_id})
        r = gmhttp.get(self.url).json()
        gmhttp.reset()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        self.assertEqual('草稿测试',r.get('data').get('content'))
        self.assertIn('diary_id',r.get('data').keys())
        self.assertIn('tags',r.get('data').keys())
        # self.assertEqual(self.tag_id1,str(r.get('data').get('tags')[0].get('tag_id')))
        print('用例执行完毕!')


    def tearDown(self):
        #清理环境，删除草稿和日志
        #删除草稿
        del_draft = g.get_info('api_info', 'draft_delete')
        url = self.host + del_draft
        gmhttp.post(url, data={'draft_id': self.draft_id})




if __name__ == "__main__":
    Draft_Detail.run()