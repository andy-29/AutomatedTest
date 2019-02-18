import gmhttp
import unittest
import os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(BASE_DIR)
from common.get_config import g





import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Draft_Create_V2(unittest.TestCase):
    '''
    批量存草稿
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

        self.user_telephone = g.get_info('user_info', 'telephone')
        self.password = g.get_info('user_info', 'password')
        # 直接使用getcookie的create_header函数，返回内容不为空则此脚本成功
        from common.getcookie import create_header
        self.header = create_header(self.user_telephone, self.password, 'android_params').get('header')
        self.assertTrue(self.header, msg='登录未成功！')
        # 首先先创建日记
        # 日记接口
        api_step1 = g.get_info('api_info', 'diary_additional_info_v1')
        url = self.host + api_step1 + "?" + self.android_params
        self.tag_id1 = g.get_info('env_info', 'tag_id1')
        r = gmhttp.post(url, data={
            'tag_ids': '[{}]'.format(self.tag_id1),
            'operation_timestamp': int(time.time()),
            'cover': '',
            'images': []
        },
                          headers=self.header,
                          verify=False)
        r = r.json()
        self.assertEqual(0, r.get('error'), msg='创建前提日记本失败！')
        self.diary_id = r.get('data').get('id')

    @data(*(get_values(func, "test_draft_create_v2")))
    def test_draft_create_v2(self,value):
        self._testMethodDoc = "--"
        '''
        批量存草稿
        '''
        url = self.host + self.api_name + "?" + self.android_params
        r = gmhttp.post(url, data={
            'draft_type': 0,  # 类型为1需要后期添加
            'content': '草稿测试',
            'cover': '',
            'diary_id': self.diary_id,
            'images': [],
            'tag_ids': '[' + self.tag_id1 + ']'
        },
                          headers=self.header,
                          verify=False)
        self.assertEqual(r.status_code, 200, '返回码不为200！')
        r = r.json()
        self.assertEqual(r.get("error"), 0)
        self.assertEqual('已保存至草稿箱', r.get('message'))
        self.assertIn('data', r.keys())
        self.assertTrue(r.get('data').get('draft_id'), msg='没有生成草稿！')
        self.draft_id = r.get('data').get('draft_id')
        self.assertTrue(r.get('data').get('create_status'))

        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Draft_Create_V2.run()