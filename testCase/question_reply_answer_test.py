from common.common import data
from common.common import cookies
from common.common import back_domain
from copy import deepcopy
from common.common import back_end_domain
from common.common import myurl
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
class Question_Reply_Answer(unittest.TestCase):
    '''
    创建回答评论
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

    @data(*(get_values(func, "test_question_reply_answer")))
    def test_question_reply_answer(self,value):
        self._testMethodDoc = "--"
        '''
        创建回答评论
        '''
        #,这个answer_id是从/hybrid/question/answer_list/_data?question_id=
        inner_data = deepcopy(data)
        post_data = {'answer_id': '601315', 'answer_reply_id': '', 'content': str(random.randint(1,100000))}
        r = gmhttp.post(url=back_end_domain + myurl['/api/question/reply_answer'],
                          params=inner_data, cookies=cookies, data=post_data)
        dict_json = json.loads(r.content.decode())
        # pprint(dict_json)
        self.assertEqual(0, dict_json['error'])


    def tearDown(self):
        pass


if __name__ == "__main__":
    Question_Reply_Answer.run()