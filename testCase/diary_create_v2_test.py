import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Diary_Create(unittest.TestCase):
    """提交操作系统时间，日志id"""

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_diary_create")))
    @require_login
    def test_diary_create(self, value):
        self._testMethodDoc = "--"
        post_data = {'diary_title': '唯美而战',
                     'operation_timestamp': str(int(time.time()))}
        r = gmhttp.post(url=self.url, data=post_data).json()
        self.assertEqual(0, r['error'],msg=r)  #本地无措，抓取linux报错


if __name__ == '__main__':
    Diary_Create.run()
