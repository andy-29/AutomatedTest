from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import back_end_domain
from pprint import pprint
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
class Hybrid_Promotion__Data(unittest.TestCase):
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

    @data(*(get_values(func, "test_hybrid_promotion__data")))
    def test_hybrid_promotion__data(self,value):
        '''
        
        '''
        # inner_data = deepcopy(data)
        # r = gmhttp.get(url=back_domain + '/hybrid/promotion/_data', params=inner_data, cookies=cookies)
        # pprint(r.content.decode())

    def tearDown(self):
        pass


if __name__ == "__main__":
    Hybrid_Promotion__Data.run()