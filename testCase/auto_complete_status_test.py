import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *


@ddt
class Auto_Complete_Status(unittest.TestCase):
    '''
    
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name

    @data(*(get_values(func, "test_auto_complete_status")))
    def test_auto_complete_status(self, value):
        self._testMethodDoc = '--'
        r = gmhttp.get(self.url).json()
        self.assertEqual(r.get("error"), 0)
        print('用例执行完毕!')

    def tearDown(self):
        pass


if __name__ == "__main__":
    Auto_Complete_Status.run()
