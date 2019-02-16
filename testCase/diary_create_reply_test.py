from common.common import data
from common.common import cookies
from common.common import back_domain
from common.common import back_end_domain
from copy import deepcopy
import unittest
import gmhttp
import json, os, time
from common.common import myurl
from common.common import thirddata
from pprint import pprint
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
class Diary_Create_Reply(unittest.TestCase):
    """
    评论日记本
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

    @data(*(get_values(func, "test_diary_create_reply")))
    def test_diary_create_reply(self,value):
        """
        评论日记本
        """
        inner_data = deepcopy(data)
        post_data = {'diary_id': thirddata['/api/diary/create_reply']['diary_id'],
                     'content':	'真的很好,真的很好{}'.format(time.ctime()),
                     'reply_id': thirddata['/api/diary/create_reply']['reply_id']}
        r = gmhttp.post(url=back_end_domain + myurl['/api/diary/create_reply'],
                          params=inner_data, data=post_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Create_Reply.run()
