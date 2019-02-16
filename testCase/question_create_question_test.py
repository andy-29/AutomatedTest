import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Post_Question(unittest.TestCase):
    """发布话题"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_post_question")))
    @require_login
    def test_post_question(self, value):
        post_data = {
            'content': '[{"type":0,"content":"有减肥项目吗"}]',
            'tags': '[' + g.get_info('env_info', 'tag_id1') + ']',
            'title': '减肥真的辛苦哦',
            "in_white_list": False,
            "city": "beijing",
            "question_type": 0,
            "is_invite_doctor": 0
        }
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'])


if __name__ == '__main__':
    Post_Question.run()
