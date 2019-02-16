import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
from  common.id_for_test import diary_id_get
@ddt
class Diary_Pre_Create_Topic(unittest.TestCase):
    '''
    发日记贴前获取预置信息
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()
    @data(*(get_values(func, "test_diary_pre_create_topic")))
    @require_login
    def test_diary_pre_create_topic(self,value):
        '''
        发日记贴前获取预置信息
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Pre_Create_Topic.run()