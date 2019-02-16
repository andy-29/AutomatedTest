from common.common import data
from common.common import back_domain
from common.common import cookies
from copy import deepcopy
import unittest
import gmhttp
import json
import os
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
class Service_Favor(unittest.TestCase):
    '''
    收藏
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        # self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

    @data(*(get_values(func, "test_service_favor")))
    def test_service_favor(self,value):
        '''
        收藏
        '''
        inner_data = deepcopy(data)
        inner_data['area_id'] = ''
        inner_data['count'] = '10'
        inner_data['current_city_id'] = 'beijing'
        inner_data['first_load'] = '0'
        inner_data['max_price'] = ''
        inner_data['min_price'] = ''
        inner_data['more_filters'] = ''
        inner_data['offset'] = ''
        inner_data['order_by'] = ''
        inner_data['tag_id'] = ''
        inner_data['tag_ids'] = ''
        r = gmhttp.get(url=back_end_domain + '/api/service/home/v3', params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json['data']['specials'][0]['services'][0]['service_id'])
        self.service_id = dict_json['data']['specials'][0]['services'][1]['service_id']
        inner_data1 = deepcopy(data)
        post_data = {}
        r1 = gmhttp.post(url=back_end_domain + '/api/service/favor/' + str(self.service_id) + '/',
                           params=inner_data1, cookies=cookies, data=post_data)
        dict_json1 = json.loads(r1.content.decode())
        # print(dict_json)
        self.assertEqual(0, dict_json1['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Favor.run()