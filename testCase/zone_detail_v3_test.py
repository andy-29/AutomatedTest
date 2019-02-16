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
        tag_id, tag_name = Zone_My().test_zone_my()
        inner_data = deepcopy(data)
        inner_data['offset'] = ''
        inner_data['size'] = '10'
        inner_data['sort_id'] = ''
        inner_data['tag_id'] = tag_id
        inner_data['zone_id'] = ''
        r = gmhttp.get(url=back_end_domain + myurl['/api/zone/detail/v3'],
                         params=inner_data, cookies=cookies)
        dict_json = json.loads(r.content.decode())
        self.assertEqual(0, dict_json['error'])

    def tearDown(self):
        pass


if __name__ == "__main__":
    Zone_Detail_V3.run()