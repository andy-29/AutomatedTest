import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone_Detail_V3(unittest.TestCase):
    '''
    圈子
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_zone_detail_v3")))
    def test_zone_detail_v3(self,value):

        gmhttp.params.update({"zone_id":zone_my_get()[0]})
        r = gmhttp.get(url=self.urls).json()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_Detail_V3.run()