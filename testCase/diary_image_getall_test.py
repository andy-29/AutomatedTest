from common.common import data
from common.common import cookies
from common.common import back_domain
from common.common import back_end_domain
from copy import deepcopy
import unittest
import gmhttp
import json, os
from common.common import myurl
from common.common import thirddata
from pprint import pprint
from testCase.user_my_diary_v2_test import My_Diary
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
class Diary_Image_Getall(unittest.TestCase):
    """

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

    @data(*(get_values(func, "test_diary_image_getall")))
    def test_diary_image_getall(self,value):
        self._testMethodDoc = "--"
        """

        """
        diary_id = My_Diary().test_my_diary()
        # pprint(diary_id)
        inner_data = deepcopy(data)
        inner_data['diary_id'] = diary_id
        inner_data['type'] = thirddata['/api/diary/image/getall']['type']
        inner_data['start_num'] = thirddata['/api/diary/image/getall']['start_num']
        inner_data['count'] = thirddata['/api/diary/image/getall']['count']
        r = gmhttp.get(url=back_end_domain + myurl['/api/diary/image/getall'],
                         cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(20009, dict_json['error_code'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Image_Getall.run()