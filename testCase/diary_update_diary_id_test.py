import gmhttp
import unittest
import os, json, time
from common.common import myurl
from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import back_end_domain
from pprint import pprint
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
class Diary_Update_Diary_Id(unittest.TestCase):
    '''
    
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

    @data(*(get_values(func, "test_diary_update_diary_id")))
    def test_diary_update_diary_id(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        inner_data_pre = deepcopy(data)
        inner_data_pre['start_num'] = '0'
        inner_data_pre['status'] = '2'
        r = gmhttp.get(url=back_end_domain + myurl['/api/orders/my/v2'],
                         params=inner_data_pre, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        diary_id = dict_json['data']['orders'][0]['buttons'][0]['url'].split('=')[1]

        # pprint(diary_id)
        inner_data = deepcopy(data)
        post_data = {'cover': '',
                     'images': '[]',
                     'tag_ids': '[]',
                     'content': '测试内容',
                     'draft_id': '',
                     'video': '',
                     'operation_timestamp': str(int(time.time()))}
        r = gmhttp.post(url=back_end_domain + myurl['/api/diary/update/{}'].format(diary_id),
                          params=inner_data, data=post_data, cookies=cookies)
        # pprint(r.content.decode())
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Update_Diary_Id.run()