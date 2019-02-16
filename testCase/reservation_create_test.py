from common.common import data
from common.common import cookies
from common.common import back_domain
from common.common import myurl
from common.common import thirddata
from copy import deepcopy
from common.common import back_end_domain
from pprint import pprint
import unittest
import gmhttp
import json, os, random

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
class Reservation_Create(unittest.TestCase):
    """
    新建预约
    """

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        print('获取环境信息和接口信息')
        self.host = g.host
        self.api_name = g.api_name(os.path.basename(__file__).split('_test.py')[0])
        self.android_params = g.android_params

    @data(*(get_values(func, "test_reservtypeation_create")))
    def test_reservtypeation_create(self,value):
        """
        新建预约,订单号硬编码
        """
        inner_data = deepcopy(data)
        post_data = {'order_id': thirddata['/api/reservation/create']['order_id'],
                     'time_frame_id': thirddata['/api/reservation/create']['time_frame_id'],
                     'type': thirddata['/api/reservation/create']['type']}
        r = gmhttp.post(url=back_end_domain + myurl['/api/reservation/create'],
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        self.assertEqual(12301, dict_json['error_code'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Reservation_Create.run()
