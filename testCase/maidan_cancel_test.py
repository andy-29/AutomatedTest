from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import back_end_domain
from pprint import pprint
import unittest
import gmhttp
import json, os
from testCase.maidan_detail_test import Maidan_Detail
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
class Maidan_Cancel(unittest.TestCase):
    '''
    买单订单取消
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

    @data(*(get_values(func, "test_maidan_cancel")))
    def test_maidan_cancel(self,value):
        '''
        买单订单取消
        '''
        order_id = Maidan_Detail().test_maidan_detail()
        inner_data = deepcopy(data)
        post_data = {'id': order_id}
        r = gmhttp.post(url=back_end_domain + '/api/maidan/cancel',
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Maidan_Cancel.run()