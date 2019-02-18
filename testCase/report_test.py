import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Report(unittest.TestCase):
    '''
    举报帖子/回复/日记本
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name
        cls.diary_id = diary_id_get()
        cls.reason_id = reason_id_get()


    @data(*(get_values(func, "test_report")))
    def test_report(self,value):
        self._testMethodDoc = "--"
        '''
        举报帖子/回复/日记本
        '''
        data = {
            "reason_id":self.reason_id,
            'diarybook_id':self.diary_id
        }
        r = gmhttp.post(self.url,data=data).json()
        self.assertEqual(r.get("error"),0)
        print('用例执行完毕!')


    def tearDown(self):
        #删除日记本
        pass


if __name__ == "__main__":
    Report.run()