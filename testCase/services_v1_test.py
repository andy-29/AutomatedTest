from common.common import data
from common.common import back_domain
from common.common import cookies
from copy import deepcopy
import unittest
import gmhttp
import json
import os
from common.common import myurl
from common.common import thirddata
from common.common import back_end_domain
from pprint import pprint
from testCase.coupon_list_my_test import Coupon_List_My
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
class Services_V1(unittest.TestCase):
    '''
    740美购列表筛选
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

    @data(*(get_values(func, "test_services_v1")))
    def test_services_v1(self,value):
        '''
        740美购列表筛选
        '''
        myid = Coupon_List_My().test_coupon_list_my()
        inner_data = deepcopy(data)
        inner_data['area_id'] = thirddata['/api/services/v1']['area_id']
        inner_data['count'] = thirddata['/api/services/v1']['count']
        inner_data['coupon_info_id'] = myid  #'14405600'
        inner_data['doctor_id'] = thirddata['/api/services/v1']['doctor_id']
        inner_data['hospital_id'] = thirddata['/api/services/v1']['hospital_id']
        inner_data['max_price'] = thirddata['/api/services/v1']['max_price']
        inner_data['min_price'] = thirddata['/api/services/v1']['min_price']
        inner_data['more_filters'] = thirddata['/api/services/v1']['more_filters']
        inner_data['offset'] = thirddata['/api/services/v1']['offset']
        inner_data['order_by'] = thirddata['/api/services/v1']['order_by']
        inner_data['tag_id'] = thirddata['/api/services/v1']['tag_id']
        inner_data['tag_ids'] = thirddata['/api/services/v1']['tag_ids']
        r = gmhttp.get(url=back_end_domain + myurl['/api/services/v1'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Services_V1.run()