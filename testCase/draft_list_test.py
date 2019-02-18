import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Draft_List(unittest.TestCase):
    '''
    获取草稿列表
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.draft_id = draft_id_get()

    @data(*(get_values(func, "test_draft_list")))
    @require_login
    def test_draft_list(self,value):
        self._testMethodDoc = "--"
        '''
        获取草稿列表
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertIn('data',r.keys())
        #直接拿字典进行对比
        # _u = {'content':'草稿测试','diary_id':str(self.diary_id),"id":self.draft_id}
        # self.assertIn(_u,[{'content':item.get('content'),'diary_id':item.get('diary_id'),"id":item.get('id')} for item in r.get('data')])
        print('用例执行完毕!')


    def tearDown(self):
        #清理环境，删除草稿和日志
        #删除草稿
        del_draft = g.get_info('api_info', 'draft_delete')
        url = self.host + del_draft
        gmhttp.post(url, data={'draft_id': self.draft_id})


if __name__ == "__main__":
    Draft_List.run()