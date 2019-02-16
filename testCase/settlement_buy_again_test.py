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
from testCase.orders_my_v2_test import Orders_My_V2




import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Settlement_Buy_Again(unittest.TestCase):
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

    @data(*(get_values(func, "test_settlement_buy_again")))
    def test_settlement_buy_again(self,value):
        '''
        
        '''
        settlement_id = Orders_My_V2().test_orders_my_v2()
        inner_data = deepcopy(data)
        post_data = {'buy_left': '0', 'id':	settlement_id}
        r = gmhttp.post(url=back_end_domain + '/api/settlement/buy_again', params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Settlement_Buy_Again.run()