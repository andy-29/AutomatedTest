from common.common import data
from common.common import cookies
from common.common import back_domain
from common.common import myurl
from copy import deepcopy
from pprint import pprint
from common.common import back_end_domain
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
class Service_Comment_Info(unittest.TestCase):
    '''
    创建评价前获取信息
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

    @data(*(get_values(func, "test_service_comment_info")))
    def test_service_comment_info(self,value):
        '''
        创建评价前获取信息
        (订单号硬编码，因为需要订单消费)
        '''
        inner_data = deepcopy(data)
        inner_data['order_id'] = '2471339004'
        r = gmhttp.get(url=back_end_domain + myurl['/api/service/comment/info'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(-1, dict_json['error_code'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Comment_Info.run()