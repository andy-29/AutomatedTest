from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import myurl
from common.common import thirddata
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
class Reservation_List(unittest.TestCase):
    """
    可用的预约时间列表
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

    @data(*(get_values(func, "test_reservation_list")))
    def test_reservation_list(self,value):
        """
        可用的预约时间列表
        （订单号硬编码，因为需要下单）
        """
        inner_data = deepcopy(data)
        inner_data['type'] = thirddata['/api/reservation/list']['type']
        inner_data['order_id'] = thirddata['/api/reservation/list']['order_id']
        r = gmhttp.get(url=back_end_domain + myurl['/api/reservation/list'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Reservation_List.run()
