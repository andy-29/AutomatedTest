from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from pprint import pprint
from common.common import myurl
from common.common import thirddata
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
class Service_Comment_Create(unittest.TestCase):
    '''
    创建美购评价
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

    @data(*(get_values(func, "test_service_comment_create")))
    def test_service_comment_create(self,value):
        self._testMethodDoc = "--"
        '''
        创建美购评价
        (订单号硬编码，因为需要订单消费)
        '''
        inner_data = deepcopy(data)
        post_data = {'order_id': thirddata['/api/service/comment/create']['order_id'],
                     'operation_effect_rating': thirddata['/api/service/comment/create']['operation_effect_rating'],
                     'doctor_attitude_rating': thirddata['/api/service/comment/create']['doctor_attitude_rating'],
                     'hospital_env_rating': thirddata['/api/service/comment/create']['hospital_env_rating'],
                     'images': thirddata['/api/service/comment/create']['images'],
                     'comment_option': thirddata['/api/service/comment/create']['comment_option'],
                     'rating': thirddata['/api/service/comment/create']['rating']}
        r = gmhttp.post(url=back_end_domain + myurl['/api/service/comment/create'],
                          params=inner_data, data=post_data, cookies=cookies)
        # pprint(r.content.decode().encode().decode('unicode-escape'))
        dict_json = json.loads(r.content.decode())
        self.assertEqual(10002, dict_json['error_code'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Service_Comment_Create.run()