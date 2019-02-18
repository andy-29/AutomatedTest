import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Report_Reason(unittest.TestCase):
    '''
    举报
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_report_reason")))
    def test_report_reason(self,value):
        self._testMethodDoc = "--"
        '''
        举报
        '''
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"),0)
        self.assertGreater(len(r.get('data')),0,msg='没有获取举报类型列表或列表为空！')
        print('用例执行完毕!')


    def tearDown(self):
        pass


if __name__ == "__main__":
    Report_Reason.run()