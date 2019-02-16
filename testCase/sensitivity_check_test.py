from copy import deepcopy

from common.common import thirddata
import json






import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Check_Centent(unittest.TestCase):
    """日记本内容检查"""
    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_check_centent")))
    @require_login
    def test_check_centent(self,value):
        post_data = {'content': thirddata['/api/sensitivity/check']['content'],
                     'filter_type': thirddata['/api/sensitivity/check']['filter_type'],
                     'isfilternum': thirddata['/api/sensitivity/check']['isfilternum']}
        r = gmhttp.post(self.url,data=post_data).json()
        self.assertEqual(0, r['error'])


if __name__ == '__main__':
    Check_Centent.run()
