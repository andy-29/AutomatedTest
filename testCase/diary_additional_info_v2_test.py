import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Diary_Additional_Info_V2(unittest.TestCase):
    '''
    日记撰写重构，新版日记本补充信息页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_diary_additional_info_v2")))
    def test_diary_additional_info_v2(self,value):
        self._testMethodDoc = "--"
        '''
        日记撰写重构，新版日记本补充信息页
        '''
        diary_id = create_diary()
        self.assertIsInstance(diary_id,int)

    def tearDown(self):
        pass


if __name__ == "__main__":
    Diary_Additional_Info_V2.run()
