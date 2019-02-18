import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
func = os.path.basename(__file__).split('_test.py')[0]
from common.gmpackage import *
@ddt
class Zone_Detail_V2(unittest.TestCase):
    '''
    圈子详情页
    '''

    @classmethod
    def setUpClass(cls):
        cls.host = g.host
        cls.api_name = g.api_name(func)
        cls.url = cls.host + cls.api_name


    @data(*(get_values(func, "test_zone_detail_v2")))
    def test_zone_detail_v2(self,value):
        self._testMethodDoc = "--"
        '''
        圈子详情页
        '''
        inner_data = {}
        inner_data['tag_id'] = '22'
        inner_data['start_num'] = '0'
        inner_data['sort_type'] = '1'
        inner_data['tab_type'] = '1'
        gmhttp.params.update(inner_data)
        r = gmhttp.get(url=self.url).json()
        gmhttp.reset()
        self.assertEqual(0, r['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_Detail_V2.run()