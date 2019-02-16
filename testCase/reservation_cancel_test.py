from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import myurl
from common.common import back_end_domain
from pprint import pprint
import unittest

import json, os, random
from testCase.reservation_mine_test import Reservation_Mine
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
class Reservation_Cancel(unittest.TestCase):
    """
    取消预约
    """

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_reservation_cancel")))
    def test_reservation_cancel(self,value):
        """
        取消预约
        """
        myid = Reservation_Mine().test_reservation_mine()
        inner_data = deepcopy(data)
        post_data = {'id': str(myid)}
        r = gmhttp.post(url=g.host + myurl['/api/reservation/cancel'],
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Reservation_Cancel.run()
