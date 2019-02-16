from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import myurl
from common.common import seconddata
from common.common import back_end_domain
from pprint import pprint
import unittest
import gmhttp
import json, os
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
class Hybrid_Topic_Topic_Id(unittest.TestCase):
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

    @data(*(get_values(func, "test_hybrid_topic_topic_id")))
    def test_hybrid_topic_topic_id(self,value):
        '''

        '''
        inner_data_pre = deepcopy(data)
        inner_data_pre[seconddata[0][0]] = seconddata[0][1]
        inner_data_pre[seconddata[1][0]] = seconddata[1][1]
        r = gmhttp.get(url=back_end_domain + myurl['/api/notification/index/v1'],
                         params=inner_data_pre, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        topic_id = dict_json['data']['push_notification'][0]['url'].split('=')[1]
        inner_data = deepcopy(data)
        inner_data['title_bar_height'] = '64'
        r = gmhttp.get(url=back_end_domain + '/hybrid/topic/{}/'.format(topic_id), params=inner_data, cookies=cookies)
        # pprint(r.content.decode())
        self.assertIn('内容详情', r.content.decode())

    def tearDown(self):
        pass


if __name__ == "__main__":
    Hybrid_Topic_Topic_Id.run()