from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import back_end_domain
from common.common import myurl
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
class Maidan_Preview(unittest.TestCase):
    '''
    买单页面
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
        inner_data = deepcopy(data)
        inner_data['search_tab'] = '3'
        r = gmhttp.get(url=back_end_domain + myurl['/api/search/keywords'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        expert = dict_json['data'][0]['url']
        if not expert:
            expert_id = ['0', '100001']
        else:
            expert_id = expert.split('=')

        self.expert_id = expert_id[1]
        return expert_id[1]

    @data(*(get_values(func, "test_maidan_preview")))
    def test_maidan_preview(self,value):
        '''
        买单页面
        '''
        inner_data = deepcopy(data)
        inner_data['doctor_id'] = self.expert_id
        r = gmhttp.get(url=back_end_domain + myurl['/api/maidan/preview'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        pprint(dict_json)
        self.assertEqual(0, dict_json['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Preview.run()