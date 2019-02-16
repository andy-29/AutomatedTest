import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Draft_Create(unittest.TestCase):
    '''
    创建草稿
    '''

    @classmethod
    def setUpClass(cls):
        print('获取环境信息和接口信息')
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()
    @data(*(get_values(func, "test_draft_create")))
    @require_login
    def test_draft_create(self, value):
        self._testMethodDoc = '创建草稿'
        value.get('requestdata').update({"diary_id":self.diary_id})
        r = gmhttp.post(self.url, data=value.get('requestdata')).json()
        self.assertTrue(r, r.update(value.get('requestdata')))
        self.draft_id = r.get('data').get('draft_id')

    def tearDown(self):
        # 删除草稿
        del_draft = g.get_info('api_info', 'draft_delete')
        url = self.host + del_draft
        gmhttp.post(url, data={'draft_id': self.draft_id})


if __name__ == "__main__":
    Draft_Create.run()
