import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Draft_Update(unittest.TestCase):
    '''
    更新草稿
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.draft_id = draft_id_get()

    @data(*(get_values(func, "test_draft_update")))
    def test_draft_update(self, value):
        '''
        更新草稿
        '''
        tag_id1 = g.get_info('env_info', 'tag_id1')
        tag_id2 = g.get_info('env_info', 'tag_id2')
        new_params = {
            'content': '草稿测试更新',
            'draft_id': self.draft_id,
            'images': [],
            'tag_ids': '[{},{}]'.format(tag_id1, tag_id2)
        }
        r = gmhttp.post(self.url, data=new_params).json()
        self.assertEqual(r.get("error"), 0)
        self.assertEqual('已保存至草稿箱', r.get('message'))
        # # 使用查看详情进行确认
        # gmhttp.params.update({"draft_id":str(self.draft_id)})
        # r = gmhttp.get(self.url).json()
        # gmhttp.reset()
        # self.assertEqual(r.get("error"), 0)
        # self.assertEqual('草稿测试更新', r.get('data').get('content'))
        # self.assertEqual({self.tag_id1, self.tag_id2}, {str(item.get("tag_id")) for item in r.get('data').get('tags')})
        # print('用例执行完毕!')

    def tearDown(self):
        # 清理环境，删除草稿和日志
        # 删除草稿
        del_draft = g.get_info('api_info', 'draft_delete')
        url = self.host + del_draft
        gmhttp.post(url, data={'draft_id': self.draft_id})


if __name__ == "__main__":
    Draft_Update.run()
