import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from common.id_for_test import diary_id_get
import time

@ddt
class Diary_Update_V2_Diary_Id(unittest.TestCase):
    '''

    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()

    @data(*(get_values(func, "test_diary_update_v2_diary_id")))
    def test_diary_update_v2_diary_id(self, value):
        '''
        更新日志
        '''
        data = {
            'tag_ids': '[]',
            'polymer_ids': '[]',
            'topic_list': '[{"content":"测试内容","images":[],"operation_timestamp":%s}]' % str(int(time.time())),
            'zone_tags': '[]'
        }
        r = gmhttp.post(self.url.format(self.diary_id,data=data)).json()
        self.assertEqual(r.get("error"), 0)
        self.assertEqual(r.get("message"), '发布成功')
        self.assertIn('data', r.keys())
        self.assertIn('status', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('status'), bool)
        self.assertIn('topic_ids', r.get('data').keys())
        self.assertIsInstance(r.get('data').get('topic_ids'), list)
        print('用例执行完毕!')

    def tearDown(self):
        # 删除日志
        # del_diary = g.get_info('api_info', 'diary_delete')
        # url = self.host + del_diary + "?" + self.android_params
        # r = gmhttp.post(url, {'diary_id': self.diary_id}, headers=self.header,
        #                   verify=False)
        # self.assertEqual(r.status_code, 200, '返回码不为200！')
        # r = r.json()
        # self.assertEqual(r.get("error"), 0)
        pass


if __name__ == "__main__":
    Diary_Update_V2_Diary_Id.run()
