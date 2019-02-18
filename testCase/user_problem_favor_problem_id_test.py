import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class User_Problem_Favor_Problem_Id(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_user_problem_favor_problem_id")))
    def test_user_problem_favor_problem_id(self,value):
        self._testMethodDoc = "--"
        '''
        
        '''
        r = gmhttp.post(url=self.url.format('3990'), data={}).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    User_Problem_Favor_Problem_Id.run()