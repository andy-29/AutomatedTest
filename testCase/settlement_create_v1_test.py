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
from testCase.shopcart_list_v2_test import Shopcart_List_V2
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
class Settlement_Create_V1(unittest.TestCase):
    '''
    创建结算单
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

    @data(*(get_values(func, "test_settlement_create_v1")))
    def test_settlement_create_v1(self,value):
        '''
        创建结算单
        '''
        mytuple = Shopcart_List_V2().test_shopcart_list_v2()
        # print(mytuple)
        inner_data = deepcopy(data)
        post_data = dict()
        post_data['cart_item_info'] = '[{"id": ' + mytuple[0] + ', "service_item_id": ' + mytuple[1] +', "number": 1}]'
        # print(post_data)
        r = gmhttp.post(url=back_end_domain + '/api/settlement/create/v1', params=inner_data, cookies=cookies,data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])
        # print(dict_json)
        print(dict_json['data']['id'])
        return dict_json['data']['id']


    def tearDown(self):
        pass


if __name__ == "__main__":
    Settlement_Create_V1.run()