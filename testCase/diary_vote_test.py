import gmhttp
import unittest
import os,json
from common.common import data
from common.common import cookies
from common.common import back_domain
from common.common import myurl
from common.common import thirddata
from copy import deepcopy
from common.common import back_end_domain
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
class Diary_Vote(unittest.TestCase):
    """
    日记本详情页点赞
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
        inner_data = deepcopy(data)
        inner_data['area_id'] = thirddata['/api/diary/cancel_vote']['area_id']
        inner_data['input_type'] = thirddata['/api/diary/cancel_vote']['input_type']
        inner_data['order_by'] = thirddata['/api/diary/cancel_vote']['order_by']
        inner_data['start_num'] = thirddata['/api/diary/cancel_vote']['start_num']
        inner_data['tag_id'] = thirddata['/api/diary/cancel_vote']['tag_id']
        inner_data['q'] = thirddata['/api/diary/cancel_vote']['q']
        r = gmhttp.get(url=back_end_domain + myurl['/api/search/v2/diary'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.diary_id = dict_json['data']['diaries'][0]['diary_id']  # 获取日记本用户号
        inner_data = deepcopy(data)
        post_data = {'diary_id': self.diary_id}
        r = gmhttp.post(url=back_end_domain + myurl['/api/diary/cancel_vote'],
                          params=inner_data, data=post_data, cookies=cookies)

    @data(*(get_values(func, "test_diary_vote")))
    def test_diary_vote(self,value):
        """
        日记本详情页点赞
        """

        # print(self.diary_id)
        inner_data1 = deepcopy(data)
        post_data1 = {'diary_id': self.diary_id}
        r1 = gmhttp.post(url=back_end_domain + myurl['/api/diary/vote'],
                           params=inner_data1, cookies=cookies, data=post_data1)
        dict_json1 = json.loads(r1.content.decode())
        self.assertEqual(0, dict_json1['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Vote.run()
