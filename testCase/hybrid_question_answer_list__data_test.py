from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import myurl
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
class Hybrid_Question_Answer_List__Data(unittest.TestCase):
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

    @data(*(get_values(func, "test_hybrid_question_answer_list__data")))
    def test_hybrid_question_answer_list__data(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        inner_data_pre = deepcopy(data)
        r = gmhttp.get(url=back_end_domain + myurl['/api/question/index/v2'],
                         params=inner_data_pre, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        question_id = dict_json['data']['topics'][0]['question_id']
        # pprint(question_id)
        inner_data = deepcopy(data)
        inner_data['page'] = '1'
        inner_data['time_sequence'] = '1'
        inner_data['question_id'] = question_id
        r = gmhttp.get(url=back_end_domain + myurl['/hybrid/question/answer_list/_data'],
                         params=inner_data, cookies=cookies)
        # pprint(r.content.decode())
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Hybrid_Question_Answer_List__Data.run()